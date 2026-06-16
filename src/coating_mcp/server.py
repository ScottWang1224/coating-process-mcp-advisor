"""FastMCP stdio server for coating process advisor tools."""

import os

os.environ.setdefault("FASTMCP_ENABLE_RICH_LOGGING", "false")
os.environ.setdefault("FASTMCP_LOG_LEVEL", "WARNING")
os.environ.setdefault("FASTMCP_SHOW_SERVER_BANNER", "false")

from fastmcp import FastMCP

from coating_mcp.tools.coating_thickness import (
    estimate_line_speed_for_target_thickness as _estimate_line_speed_for_target_thickness,
)
from coating_mcp.tools.process_range import check_process_range as _check_process_range
from coating_mcp.tools.solvent_adjustment import (
    calculate_solvent_addition as _calculate_solvent_addition,
)
from coating_mcp.tools.unit_conversion import (
    convert_temperature as _convert_temperature,
    convert_volume as _convert_volume,
)
from coating_mcp.tools.viscosity_risk import (
    estimate_viscosity_temperature_risk as _estimate_viscosity_temperature_risk,
)

mcp = FastMCP("coating-process")


@mcp.tool
def convert_volume(value: float, from_unit: str, to_unit: str) -> dict[str, float | str]:
    """Convert volume between mL, L, and m3 for simulation-only process checks."""
    return _convert_volume(value, from_unit, to_unit)


@mcp.tool
def convert_temperature(value: float, from_unit: str, to_unit: str) -> dict[str, float | str]:
    """Convert temperature between C, K, and F for simulation-only process checks."""
    return _convert_temperature(value, from_unit, to_unit)


@mcp.tool
def check_process_range(
    parameter_name: str,
    current_value: float,
    lower_limit: float,
    upper_limit: float,
    unit: str,
) -> dict[str, float | str]:
    """Check if a simulated process parameter is normal, low, or high."""
    return _check_process_range(parameter_name, current_value, lower_limit, upper_limit, unit)


@mcp.tool
def calculate_solvent_addition(
    initial_volume: float,
    current_concentration: float,
    target_concentration: float,
    volume_unit: str = "L",
    concentration_unit: str = "wt%",
) -> dict[str, float | str]:
    """Estimate solvent addition using a simple simulation-only dilution balance."""
    return _calculate_solvent_addition(
        initial_volume,
        current_concentration,
        target_concentration,
        volume_unit,
        concentration_unit,
    )


@mcp.tool
def estimate_line_speed_for_target_thickness(
    current_thickness: float,
    target_thickness: float,
    current_speed: float,
    thickness_unit: str = "um",
    speed_unit: str = "m/min",
) -> dict[str, float | str]:
    """Estimate line speed for a target coating thickness using inverse proportionality."""
    return _estimate_line_speed_for_target_thickness(
        current_thickness,
        target_thickness,
        current_speed,
        thickness_unit,
        speed_unit,
    )


@mcp.tool
def estimate_viscosity_temperature_risk(
    current_viscosity: float,
    viscosity_lower_limit: float,
    viscosity_upper_limit: float,
    current_temperature: float,
    standard_temperature: float,
    viscosity_unit: str = "cP",
    temperature_unit: str = "C",
) -> dict[str, str]:
    """Estimate qualitative viscosity risk from viscosity and temperature context."""
    return _estimate_viscosity_temperature_risk(
        current_viscosity,
        viscosity_lower_limit,
        viscosity_upper_limit,
        current_temperature,
        standard_temperature,
        viscosity_unit,
        temperature_unit,
    )


def main() -> None:
    mcp.run(
        transport="stdio",
        show_banner=False,
        log_level="WARNING",
    )


if __name__ == "__main__":
    main()
