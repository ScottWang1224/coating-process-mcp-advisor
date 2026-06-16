"""Output schemas for coating process tools."""

from pydantic import BaseModel


class ConversionOutput(BaseModel):
    converted_value: float
    unit: str


class ProcessRangeOutput(BaseModel):
    parameter_name: str
    status: str
    deviation: float
    message: str


class SolventAdditionOutput(BaseModel):
    initial_volume: float
    final_volume: float
    solvent_to_add: float
    volume_unit: str
    current_concentration: float
    target_concentration: float
    concentration_unit: str
    assumption: str


class LineSpeedOutput(BaseModel):
    recommended_speed: float
    speed_unit: str
    current_thickness: float
    target_thickness: float
    current_speed: float
    thickness_unit: str
    assumption: str


class ViscosityRiskOutput(BaseModel):
    status: str
    risk_level: str
    possible_reason: str
    recommendation: str
    note: str

