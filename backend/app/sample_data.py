from app.schemas import Machine, MachineStatus
machines: list[Machine] = [
    Machine(
        id=1,
        name="Conveyor A",
        status=MachineStatus.RUNNING,
    ),
    Machine(
        id=2,
        name="Hydraulic Press",
        status=MachineStatus.IDLE,
    ),
]