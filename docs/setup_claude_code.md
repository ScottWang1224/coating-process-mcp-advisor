# Claude Code Setup

Install the package in your project environment:

```bash
pip install .
```

Then add the example from `clients/claude-code/mcp.example.json` to your Claude Code MCP
configuration.

Prefer the installed entrypoint:

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

On Windows with the venv at `C:\venvs\coating-mcp`, use:

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
