# Architecture

```text
User scenario
  -> Agent client
  -> skill instructions
  -> MCP client
  -> FastMCP stdio server
  -> deterministic Python tool
  -> calculation result
  -> simulation-only Agent response
```

The calculation logic lives in `src/coating_mcp/tools`. The MCP server in
`src/coating_mcp/server.py` only registers those functions as tools, so tests and runtime behavior
share the same implementation.

