# Agent Instructions

This project provides a simulated coating process MCP advisor.

Before answering coating process questions, read:

`skills/coating_process_advisor_skill.md`

Rules:

1. Use MCP tools for supported calculations.
2. Do not calculate manually if a matching MCP tool exists.
3. Do not invent missing physical properties.
4. Do not use real company data, real machine names, or real formulas from proprietary processes.
5. Always mark advice as simulation-only.
6. Always include:
   - process status
   - known process conditions
   - possible reason
   - tool used
   - calculation result
   - simulated operation suggestion
   - notes

