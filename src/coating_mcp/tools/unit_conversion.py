"""Unit conversion tools for simulated coating process support."""

VOLUME_TO_LITERS = {
    "mL": 0.001,
    "L": 1.0,
    "m3": 1000.0,
}


def convert_volume(value: float, from_unit: str, to_unit: str) -> dict[str, float | str]:
    """Convert a volume between mL, L, and m3.

    Args:
        value: Non-negative volume value.
        from_unit: Source unit. Supported units: mL, L, m3.
        to_unit: Target unit. Supported units: mL, L, m3.

    Returns:
        A dictionary containing converted_value and unit.

    Raises:
        ValueError: If the value is negative or either unit is unsupported.
    """
    if value < 0:
        raise ValueError("value must be greater than or equal to 0")
    if from_unit not in VOLUME_TO_LITERS:
        raise ValueError(f"unsupported from_unit: {from_unit}")
    if to_unit not in VOLUME_TO_LITERS:
        raise ValueError(f"unsupported to_unit: {to_unit}")

    liters = value * VOLUME_TO_LITERS[from_unit]
    converted_value = liters / VOLUME_TO_LITERS[to_unit]
    return {"converted_value": round(converted_value, 6), "unit": to_unit}


def convert_temperature(value: float, from_unit: str, to_unit: str) -> dict[str, float | str]:
    """Convert a temperature between C, K, and F.

    Args:
        value: Temperature value.
        from_unit: Source unit. Supported units: C, K, F.
        to_unit: Target unit. Supported units: C, K, F.

    Returns:
        A dictionary containing converted_value and unit.

    Raises:
        ValueError: If a unit is unsupported or Kelvin would be below 0.
    """
    supported = {"C", "K", "F"}
    if from_unit not in supported:
        raise ValueError(f"unsupported from_unit: {from_unit}")
    if to_unit not in supported:
        raise ValueError(f"unsupported to_unit: {to_unit}")

    if from_unit == "C":
        celsius = value
    elif from_unit == "K":
        if value < 0:
            raise ValueError("Kelvin value must be greater than or equal to 0")
        celsius = value - 273.15
    else:
        celsius = (value - 32) * 5 / 9

    kelvin = celsius + 273.15
    if kelvin < 0:
        raise ValueError("temperature cannot be below absolute zero")

    if to_unit == "C":
        converted_value = celsius
    elif to_unit == "K":
        converted_value = kelvin
    else:
        converted_value = celsius * 9 / 5 + 32

    return {"converted_value": round(converted_value, 6), "unit": to_unit}

