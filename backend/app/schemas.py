from enum import Enum

from pydantic import BaseModel, Field


class MachineStatus(str, Enum):
    RUNNING = "running"
    IDLE = "idle"
    STOPPED = "stopped"


class Machine(BaseModel):
    id: int = Field(gt=0)
    name: str = Field(min_length=1, max_length=100)
    status: MachineStatus