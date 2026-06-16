import pytest

from coating_mcp.tools.unit_conversion import convert_temperature, convert_volume


def test_convert_volume_ml_to_l() -> None:
    assert convert_volume(500, "mL", "L") == {"converted_value": 0.5, "unit": "L"}


def test_convert_temperature_c_to_k() -> None:
    assert convert_temperature(25, "C", "K") == {"converted_value": 298.15, "unit": "K"}


def test_convert_volume_rejects_unsupported_unit() -> None:
    with pytest.raises(ValueError, match="unsupported"):
        convert_volume(1, "gal", "L")


def test_convert_temperature_rejects_below_absolute_zero() -> None:
    with pytest.raises(ValueError, match="absolute zero"):
        convert_temperature(-274, "C", "K")

