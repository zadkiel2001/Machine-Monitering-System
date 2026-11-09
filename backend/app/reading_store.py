from app.schemas import SensorReading
class ReadingStore:
    """Keep the most recently saved reading for each machine."""
    def __init__(self) -> None:
        self._latest: dict[int, SensorReading] = {}
    def save(self, reading: SensorReading) -> None:
        self._latest[reading.machine_id] = reading
    def get_latest(self, machine_id: int) -> SensorReading | None:
        return self._latest.get(machine_id)