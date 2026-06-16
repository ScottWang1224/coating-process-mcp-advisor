"""Coating thickness and line speed estimates."""


def estimate_line_speed_for_target_thickness(
    current_thickness: float,
    target_thickness: float,
    current_speed: float,
    thickness_unit: str = "um",
    speed_unit: str = "m/min",
) -> dict[str, float | str]:
    """Estimate line speed needed to reach a target coating thickness.

    Formula:
        target_speed = current_thickness * current_speed / target_thickness

    This simulation assumes inverse proportionality between wet thickness and line speed while
    keeping other process variables unchanged.
    """
    if current_thickness <= 0:
        raise ValueError("current_thickness must be greater than 0")
    if target_thickness <= 0:
        raise ValueError("target_thickness must be greater than 0")
    if current_speed <= 0:
        raise ValueError("current_speed must be greater than 0")

    recommended_speed = current_thickness * current_speed / target_thickness
    return {
        "recommended_speed": round(recommended_speed, 2),
        "speed_unit": speed_unit,
        "current_thickness": round(current_thickness, 6),
        "target_thickness": round(target_thickness, 6),
        "current_speed": round(current_speed, 6),
        "thickness_unit": thickness_unit,
        "assumption": (
            "Simulation-only estimate; assumes thickness is inversely proportional to line speed "
            "with coating gap, solids, viscosity, and drying conditions unchanged."
        ),
    }

