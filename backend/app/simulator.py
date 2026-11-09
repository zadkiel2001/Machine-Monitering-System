from datetime import datetime, timezone
from random import Random
from app.schemas import Machine, MachineStatus, SensorReading
def generate_reading(machine: Machine, rng: Random) -> SensorReading:
    """Generate a sample reading based on the machine's status."""
    if machine.status == MachineStatus.RUNNING:
        temperature_c = rng.uniform(55.0, 75.0)
        vibration_mm_s = rng.uniform(1.0, 3.0)
    elif machine.status == MachineStatus.IDLE:
        temperature_c = rng.uniform(30.0, 45.0)
        vibration_mm_s = rng.uniform(0.1, 0.5)
    else:
        temperature_c = rng.uniform(22.0, 30.0)
        vibration_mm_s = 0.0
    return SensorReading(
        machine_id=machine.id,
        timestamp=datetime.now(timezone.utc),
        temperature_c=round(temperature_c, 2),
        vibration_mm_s=round(vibration_mm_s, 2),
    )