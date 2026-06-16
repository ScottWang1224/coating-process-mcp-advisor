# Coating Process MCP Advisor

一個以 **FastMCP** 建立的塗佈製程模擬輔助工具。  
它提供可重複、可測試的 Python 計算工具，讓 Codex、Claude Code 或其他支援 MCP 的 Agent 可以透過 tool call 協助判斷塗佈製程中的基礎數值問題。

> 注意：本專案僅供 **simulation-only** 的示範與輔助計算，不是實際生產操作指引。

## 專案目標

將常見的基礎計算與範圍判斷交給 MCP tools，讓 Agent 回答時不要憑空推論或手算錯誤。

目前適合處理的問題類型：

- 黏度、固含、膜厚等參數是否超出上下限
- 體積與溫度單位換算
- 固含偏高時，估算需要加入多少溶劑
- 膜厚偏厚或偏薄時，估算線速調整方向
- 黏度異常時，根據溫度情境做初步風險分類

目前不處理：

- 真實配方建議
- 真實產線操作決策
- 專有製程資料
- 缺陷診斷，例如縮孔、條紋、氣泡、橘皮
- RAG、PDF、OCR、資料庫或 Web UI

## 功能

- 體積換算：`mL`、`L`、`m3`
- 溫度換算：`C`、`K`、`F`
- 製程範圍判斷：`normal`、`low`、`high`
- 溶劑添加量估算
- 目標膜厚對應線速估算
- 黏度與溫度風險分類
- pytest 測試
- YAML 範例情境與 CLI demo
- FastMCP stdio server
- Codex / Claude Code / generic MCP 設定範例
- Dockerfile

## 安裝

建議使用 Python 3.11 以上。

Windows 若專案路徑包含中文或非 ASCII 字元，建議把虛擬環境建立在純英文路徑，例如 `C:\venvs\coating-mcp`。

```powershell
$env:PYTHONNOUSERSITE="1"
$env:PYTHONUTF8="1"
py -3.11 -X utf8 -m venv C:\venvs\coating-mcp
C:\venvs\coating-mcp\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install ".[dev]"
```

請避免在中文路徑下使用 editable install：

```powershell
python -m pip install -e ".[dev]"
```

editable install 會產生 `.pth` 檔，在 Windows CP950 環境中可能造成解碼錯誤。

## 測試

```powershell
python -m pytest
```

預期結果：

```text
18 passed
```

## 執行範例情境

```powershell
python -m coating_mcp.cli.run_examples
```

或使用安裝後的 entrypoint：

```powershell
coating-mcp-examples
```

目前範例包含：

- 固含偏高，估算溶劑添加量
- 膜厚偏厚，估算建議線速
- 黏度偏高且溫度偏低，判斷風險

## 啟動 MCP Server

```powershell
coating-mcp
```

MCP server 已針對 Agent stdio 使用情境做過設定：

- 關閉 FastMCP banner
- log level 設為 `WARNING`
- 預設關閉 rich logging
- server 啟動時不使用 `print()` 輸出 debug 訊息

請不要在 `src/coating_mcp/server.py` 裡加入 `print()` debug。  
stdio MCP server 的 stdout 必須保留給 MCP JSON-RPC protocol；診斷訊息應走 stderr logging 或檔案。

## MCP Tools

| Tool | 用途 |
| --- | --- |
| `convert_volume` | 在 `mL`、`L`、`m3` 之間換算體積。 |
| `convert_temperature` | 在 `C`、`K`、`F` 之間換算溫度。 |
| `check_process_range` | 判斷製程參數是 `normal`、`low` 或 `high`。 |
| `calculate_solvent_addition` | 估算降低濃度所需添加的溶劑量。 |
| `estimate_line_speed_for_target_thickness` | 依目標膜厚估算建議線速。 |
| `estimate_viscosity_temperature_risk` | 依黏度範圍與溫度情境做定性風險分類。 |

## Codex MCP 設定

完整範例請看 [clients/codex/config.example.toml](clients/codex/config.example.toml)。

若 `coating-mcp` 已在 PATH 中，可以使用：

```toml
[mcp_servers.coating-process]
command = "coating-mcp"
args = []
startup_timeout_sec = 20

[mcp_servers.coating-process.env]
PYTHONUTF8 = "1"
PYTHONIOENCODING = "utf-8"
FASTMCP_SHOW_SERVER_BANNER = "false"
FASTMCP_ENABLE_RICH_LOGGING = "false"
FASTMCP_LOG_LEVEL = "WARNING"
```

Windows venv 建議使用絕對路徑：

```toml
[mcp_servers.coating-process]
command = "C:\\venvs\\coating-mcp\\Scripts\\coating-mcp.exe"
args = []
startup_timeout_sec = 20

[mcp_servers.coating-process.env]
PYTHONUTF8 = "1"
PYTHONIOENCODING = "utf-8"
PYTHONNOUSERSITE = "1"
FASTMCP_SHOW_SERVER_BANNER = "false"
FASTMCP_ENABLE_RICH_LOGGING = "false"
FASTMCP_LOG_LEVEL = "WARNING"
```

設定後重啟 Codex，並用以下方式檢查 MCP server：

```powershell
codex mcp --help
codex mcp list
```

在 Codex TUI 內也可以使用：

```text
/mcp
```

測試提問範例：

```text
目前塗液黏度 850 cP，規格範圍是 500 到 700 cP。請用 coating-process MCP tool 判斷狀態與偏差。
```

## Claude Code MCP 設定

完整範例請看 [clients/claude-code/mcp.example.json](clients/claude-code/mcp.example.json)。

```json
{
  "mcpServers": {
    "coating-process": {
      "command": "coating-mcp",
      "args": [],
      "env": {
        "PYTHONUTF8": "1",
        "PYTHONIOENCODING": "utf-8",
        "FASTMCP_SHOW_SERVER_BANNER": "false",
        "FASTMCP_ENABLE_RICH_LOGGING": "false",
        "FASTMCP_LOG_LEVEL": "WARNING"
      }
    }
  }
}
```

Windows venv 範例：

```json
{
  "mcpServers": {
    "coating-process": {
      "command": "C:\\venvs\\coating-mcp\\Scripts\\coating-mcp.exe",
      "args": [],
      "env": {
        "PYTHONUTF8": "1",
        "PYTHONIOENCODING": "utf-8",
        "PYTHONNOUSERSITE": "1",
        "FASTMCP_SHOW_SERVER_BANNER": "false",
        "FASTMCP_ENABLE_RICH_LOGGING": "false",
        "FASTMCP_LOG_LEVEL": "WARNING"
      }
    }
  }
}
```

## Docker

```bash
docker build -t coating-process-mcp:latest .
docker run --rm -i coating-process-mcp:latest
```

## 安全與限制

- 所有輸出都是 simulation-only。
- 不推論缺失的物性資料，例如密度、蒸發速率、比熱、剪切黏度曲線。
- 不使用真實公司資料、真實機台名稱或專有配方。
- 不提供未經驗證的實際生產操作建議。
- 實際製程調整仍需由合格工程師與正式 SOP 確認。
