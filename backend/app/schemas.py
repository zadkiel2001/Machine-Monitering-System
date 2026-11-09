from enum import Enum
from pydantic import AwareDatetime, BaseModel, Field
class MachineStatus(str, Enum):
    RUNNING = "running"
    IDLE = "idle"
    STOPPED = "stopped"
class Machine(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=1, max_length=100)
    status: MachineStatus
class SensorReading(BaseModel):
    machine_id: int = Field(gt=0)
    timestamp: AwareDatetime
    temperature_c: float = Field(
        ge=-273.15,
        allow_inf_nan=False,
    )
    vibration_mm_s: float = Field(
        ge=0,
        allow_inf_nan=False,
    )