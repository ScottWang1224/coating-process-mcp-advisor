"""Input schemas for coating process tools."""

from pydantic import BaseModel, Field


class VolumeConversionInput(BaseModel):
    value: float = Field(ge=0)
    from_unit: str
    to_unit: str


class TemperatureConversionInput(BaseModel):
    value: float
    from_unit: str
    to_unit: str


class ProcessRangeInput(BaseModel):
    parameter_name: str
    current_value: float
    lower_limit: float
    upper_limit: float
    unit: str


class SolventAdditionInput(BaseModel):
    initial_volume: float = Field(gt=0)
    current_concentration: float = Field(gt=0)
    target_concentration: float = Field(gt=0)
    volume_unit: str = "L"
    concentration_unit: str = "wt%"


class LineSpeedInput(BaseModel):
    current_thickness: float = Field(gt=0)
    target_thickness: float = Field(gt=0)
    current_speed: float = Field(gt=0)
    thickness_unit: str = "um"
    speed_unit: str = "m/min"


class ViscosityRiskInput(BaseModel):
    current_viscosity: float = Field(gt=0)
    viscosity_lower_limit: float
    viscosity_upper_limit: float
    current_temperature: float
    standard_temperature: float
    viscosity_unit: str = "cP"
    temperature_unit: str = "C"

