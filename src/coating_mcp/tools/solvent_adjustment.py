"""Solvent addition estimates for simulated coating process support."""


def calculate_solvent_addition(
    initial_volume: float,
    current_concentration: float,
    target_concentration: float,
    volume_unit: str = "L",
    concentration_unit: str = "wt%",
) -> dict[str, float | str]:
    """Estimate solvent addition using a simple dilution balance.

    Formula:
        V_final = V_initial * C_current / C_target
        V_solvent_add = V_final - V_initial

    This simulation assumes concentration reduction is caused only by adding compatible solvent.
    It does not account for density change, evaporation, reaction, retained solids, or equipment loss.
    """
    if initial_volume <= 0:
        raise ValueError("initial_volume must be greater than 0")
    if current_concentration <= 0:
        raise ValueError("current_concentration must be greater than 0")
    if target_concentration <= 0:
        raise ValueError("target_concentration must be greater than 0")
    if target_concentration >= current_concentration:
        raise ValueError(
            "target_concentration must be lower than current_concentration for solvent addition"
        )

    final_volume = initial_volume * current_concentration / target_concentration
    solvent_to_add = final_volume - initial_volume
    return {
        "initial_volume": round(initial_volume, 6),
        "final_volume": round(final_volume, 2),
        "solvent_to_add": round(solvent_to_add, 2),
        "volume_unit": volume_unit,
        "current_concentration": round(current_concentration, 6),
        "target_concentration": round(target_concentration, 6),
        "concentration_unit": concentration_unit,
        "assumption": (
            "Simulation-only dilution estimate; assumes solvent addition is the only change and "
            "does not account for density, evaporation, or production-specific properties."
        ),
    }

