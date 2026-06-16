# Codex Setup

Install the package in your project environment:

```bash
pip install .
```

Then add the example from `clients/codex/config.example.toml` to your Codex MCP configuration.
Codex reads MCP configuration from `~/.codex/config.toml`, or from project-scoped
`.codex/config.toml` in trusted projects.

## Recommended Config

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

## Windows Venv Config

Use this when the package is installed in `C:\venvs\coating-mcp` and `coating-mcp` is not on PATH:

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

## Smoke Test

```bash
python -c "import coating_mcp.server; print('mcp server import ok')"
```

Then restart Codex and check MCP status with one of:

```bash
codex mcp --help
codex mcp list
```

Inside the Codex TUI, use:

```text
/mcp
```

Ask a tool-backed question:

```text
目前塗液黏度 850 cP，規格範圍是 500 到 700 cP。請用 coating-process MCP tool 判斷狀態與偏差。
```
