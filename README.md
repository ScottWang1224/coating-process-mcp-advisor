# Coating Process MCP Advisor

Simulation-only MCP tools for coating process advisory workflows.

This project provides deterministic Python calculation tools and a FastMCP stdio server that an
Agent client such as Codex or Claude Code can call when answering simulated coating process
questions. It is not production guidance and must not be used with proprietary formulas or real
factory control decisions.

## Features

- Volume conversion: `mL`, `L`, `m3`
- Temperature conversion: `C`, `K`, `F`
- Process range status: `normal`, `low`, `high`
- Solvent addition estimate for concentration reduction
- Line speed estimate for target coating thickness
- Qualitative viscosity and temperature risk classification
- Pytest coverage for all MVP tools
- Example scenarios and deterministic CLI demo
- FastMCP stdio server
- Codex, Claude Code, generic MCP config examples

## Setup

```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install ".[dev]"
```

On Windows paths containing non-ASCII characters, prefer a virtual environment in an ASCII-only
path such as `C:\venvs\coating-mcp` and avoid editable installs. Editable installs create a `.pth`
file that may fail to decode under CP950.

## Run Tests

```bash
pytest
```

## Run Example Demo

```bash
python -m coating_mcp.cli.run_examples
```

## Run MCP Server

```bash
coating-mcp
```

The MCP server is configured for agent-friendly stdio startup:

- server banner disabled
- log level set to `WARNING`
- rich logging disabled by default
- no debug `print()` calls from the stdio server

Do not add `print()` debugging to `src/coating_mcp/server.py`; stdout is reserved for MCP
JSON-RPC messages. Use stderr logging or files for diagnostics.

## MCP Tools

| Tool | Purpose |
| --- | --- |
| `convert_volume` | Convert volume between `mL`, `L`, and `m3`. |
| `convert_temperature` | Convert temperature between `C`, `K`, and `F`. |
| `check_process_range` | Check whether a process parameter is normal, low, or high. |
| `calculate_solvent_addition` | Estimate solvent needed to lower concentration. |
| `estimate_line_speed_for_target_thickness` | Estimate line speed for a target thickness. |
| `estimate_viscosity_temperature_risk` | Classify qualitative viscosity risk using temperature context. |

## Codex MCP Example

See [clients/codex/config.example.toml](clients/codex/config.example.toml).

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

Windows virtual environment example:

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

Check your Codex MCP setup with `codex mcp --help`, `codex mcp list` if available in your
installed Codex version, or `/mcp` inside the Codex TUI.

## Claude Code MCP Example

See [clients/claude-code/mcp.example.json](clients/claude-code/mcp.example.json).

```json
{
  "mcpServers": {
    "coating-process": {
      "command": "python",
      "args": ["-m", "coating_mcp.server"]
    }
  }
}
```

## Docker

```bash
docker build -t coating-process-mcp:latest .
docker run --rm -i coating-process-mcp:latest
```

## Safety Notes

- All outputs are simulation-only.
- Do not infer missing physical properties.
- Do not use real company data, real machine names, or proprietary formulas.
- Confirm actual process changes with qualified process engineers and approved procedures.
