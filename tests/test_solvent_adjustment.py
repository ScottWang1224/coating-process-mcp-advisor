import pytest

from coating_mcp.tools.solvent_adjustment import calculate_solvent_addition


def test_calculate_solvent_addition() -> None:
    result = calculate_solvent_addition(800, 26, 22)
    assert result["final_volume"] == 945.45
    assert result["solvent_to_add"] == 145.45
    assert result["volume_unit"] == "L"


def test_calculate_solvent_addition_rejects_target_not_lower() -> None:
    with pytest.raises(ValueError, match="target_concentration"):
        calculate_solvent_addition(800, 22, 26)


def test_calculate_solvent_addition_rejects_zero_volume() -> None:
    with pytest.raises(ValueError, match="initial_volume"):
        calculate_solvent_addition(0, 26, 22)

