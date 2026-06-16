import pytest

from coating_mcp.tools.process_range import check_process_range


def test_process_range_high() -> None:
    result = check_process_range("viscosity", 850, 500, 700, "cP")
    assert result["status"] == "high"
    assert result["deviation"] == 150


def test_process_range_normal() -> None:
    result = check_process_range("viscosity", 600, 500, 700, "cP")
    assert result["status"] == "normal"
    assert result["deviation"] == 0


def test_process_range_low() -> None:
    result = check_process_range("viscosity", 450, 500, 700, "cP")
    assert result["status"] == "low"
    assert result["deviation"] == 50


def test_process_range_rejects_invalid_limits() -> None:
    with pytest.raises(ValueError, match="lower_limit"):
        check_process_range("viscosity", 600, 700, 500, "cP")

