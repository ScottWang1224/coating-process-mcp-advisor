"""Run deterministic example scenarios without an LLM."""

from __future__ import annotations

from pathlib import Path

import yaml

from coating_mcp.tools import (
    calculate_solvent_addition,
    check_process_range,
    estimate_line_speed_for_target_thickness,
    estimate_viscosity_temperature_risk,
)


def main() -> None:
    scenarios_path = _find_scenarios_path()
    scenarios = yaml.safe_load(scenarios_path.read_text(encoding="utf-8"))

    for scenario in scenarios:
        print(f"\n[{scenario['id']}] {scenario['title']}")
        print(f"Prompt: {scenario['user_prompt']}")
        print(f"Expected tools: {', '.join(scenario['expected_tools'])}")
        print("Deterministic demo result:")
        print(_run_demo_for_scenario(scenario["id"]))


def _run_demo_for_scenario(scenario_id: str) -> dict[str, object]:
    if scenario_id == "high_solid_content_001":
        return {
            "range": check_process_range("solid_content", 26, 20, 22, "wt%"),
            "solvent": calculate_solvent_addition(800, 26, 22),
        }
    if scenario_id == "coating_thickness_high_001":
        return {"line_speed": estimate_line_speed_for_target_thickness(8, 6, 10)}
    if scenario_id == "viscosity_high_001":
        return {
            "range": check_process_range("viscosity", 850, 500, 700, "cP"),
            "risk": estimate_viscosity_temperature_risk(850, 500, 700, 20, 25),
        }
    raise ValueError(f"unknown scenario id: {scenario_id}")


def _find_scenarios_path() -> Path:
    candidates = [
        Path.cwd() / "examples" / "scenarios.yaml",
        Path(__file__).resolve().parents[3] / "examples" / "scenarios.yaml",
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    searched = ", ".join(str(candidate) for candidate in candidates)
    raise FileNotFoundError(f"examples/scenarios.yaml not found. Searched: {searched}")


if __name__ == "__main__":
    main()
