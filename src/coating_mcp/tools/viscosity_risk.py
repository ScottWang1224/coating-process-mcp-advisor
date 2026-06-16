"""Viscosity and temperature risk estimates for simulated coating process support."""


def estimate_viscosity_temperature_risk(
    current_viscosity: float,
    viscosity_lower_limit: float,
    viscosity_upper_limit: float,
    current_temperature: float,
    standard_temperature: float,
    viscosity_unit: str = "cP",
    temperature_unit: str = "C",
) -> dict[str, str]:
    """Estimate qualitative viscosity risk using measured viscosity and temperature context.

    This tool does not calculate a corrected viscosity. It only classifies a simulated process
    condition using the rules defined in the project PRD.
    """
    if current_viscosity <= 0:
        raise ValueError("current_viscosity must be greater than 0")
    if viscosity_lower_limit > viscosity_upper_limit:
        raise ValueError("viscosity_lower_limit must be less than or equal to viscosity_upper_limit")

    if viscosity_lower_limit <= current_viscosity <= viscosity_upper_limit:
        return {
            "status": "normal",
            "risk_level": "low",
            "possible_reason": "viscosity is within the simulated control range",
            "recommendation": "keep monitoring",
            "note": _note(viscosity_unit, temperature_unit),
        }

    if current_viscosity > viscosity_upper_limit:
        if current_temperature < standard_temperature:
            return {
                "status": "high",
                "risk_level": "medium",
                "possible_reason": "lower temperature may increase viscosity",
                "recommendation": (
                    "bring temperature back to the standard condition and re-check viscosity "
                    "before adding solvent"
                ),
                "note": _note(viscosity_unit, temperature_unit),
            }
        return {
            "status": "high",
            "risk_level": "high",
            "possible_reason": "possible high solid content or solvent evaporation",
            "recommendation": "check solid content and solvent loss before adjustment",
            "note": _note(viscosity_unit, temperature_unit),
        }

    return {
        "status": "low",
        "risk_level": "medium",
        "possible_reason": "possible excess solvent or low solid content",
        "recommendation": "check solid content before adding resin or changing speed",
        "note": _note(viscosity_unit, temperature_unit),
    }


def _note(viscosity_unit: str, temperature_unit: str) -> str:
    return (
        "Simulation-only qualitative risk classification. This tool does not infer real material "
        f"properties or proprietary process behavior. Units: {viscosity_unit}, {temperature_unit}."
    )

