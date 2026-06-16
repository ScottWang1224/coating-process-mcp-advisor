import pytest

from coating_mcp.tools.coating_thickness import estimate_line_speed_for_target_thickness


def test_estimate_line_speed_for_target_thickness() -> None:
    result = estimate_line_speed_for_target_thickness(8, 6, 10)
    assert result["recommended_speed"] == 13.33
    assert result["speed_unit"] == "m/min"


def test_estimate_line_speed_rejects_zero_target_thickness() -> None:
    with pytest.raises(ValueError, match="target_thickness"):
        estimate_line_speed_for_target_thickness(8, 0, 10)


def test_estimate_line_speed_rejects_zero_speed() -> None:
    with pytest.raises(ValueError, match="current_speed"):
        estimate_line_speed_for_target_thickness(8, 6, 0)

