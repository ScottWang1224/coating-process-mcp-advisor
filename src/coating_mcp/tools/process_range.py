"""Process range checks for simulated coating process support."""


def check_process_range(
    parameter_name: str,
    current_value: float,
    lower_limit: float,
    upper_limit: float,
    unit: str,
) -> dict[str, float | str]:
    """Check whether a process parameter is inside a configured range.

    Args:
        parameter_name: Name of the process parameter.
        current_value: Current measured value.
        lower_limit: Lower acceptable limit.
        upper_limit: Upper acceptable limit.
        unit: Unit label for the value.

    Returns:
        A dictionary containing parameter_name, status, deviation, and message.
    """
    if lower_limit > upper_limit:
        raise ValueError("lower_limit must be less than or equal to upper_limit")

    if current_value < lower_limit:
        deviation = lower_limit - current_value
        status = "low"
        message = f"{parameter_name} is below lower limit by {deviation:g} {unit}"
    elif current_value > upper_limit:
        deviation = current_value - upper_limit
        status = "high"
        message = f"{parameter_name} is above upper limit by {deviation:g} {unit}"
    else:
        deviation = 0.0
        status = "normal"
        message = f"{parameter_name} is within range"

    return {
        "parameter_name": parameter_name,
        "status": status,
        "deviation": round(deviation, 6),
        "message": message,
    }

