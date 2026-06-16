from coating_mcp.tools.viscosity_risk import estimate_viscosity_temperature_risk


def test_high_viscosity_lower_temperature_is_medium_risk() -> None:
    result = estimate_viscosity_temperature_risk(850, 500, 700, 20, 25)
    assert result["status"] == "high"
    assert result["risk_level"] == "medium"
    assert "temperature" in result["possible_reason"]


def test_high_viscosity_standard_temperature_is_high_risk() -> None:
    result = estimate_viscosity_temperature_risk(850, 500, 700, 25, 25)
    assert result["status"] == "high"
    assert result["risk_level"] == "high"


def test_normal_viscosity_is_low_risk() -> None:
    result = estimate_viscosity_temperature_risk(600, 500, 700, 25, 25)
    assert result["status"] == "normal"
    assert result["risk_level"] == "low"


def test_low_viscosity_is_medium_risk() -> None:
    result = estimate_viscosity_temperature_risk(450, 500, 700, 25, 25)
    assert result["status"] == "low"
    assert result["risk_level"] == "medium"

