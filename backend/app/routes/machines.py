from fastapi import APIRouter, HTTPException, Path

from app.schemas import Machine, MachineStatus


router = APIRouter(
    prefix="/machines",
    tags=["Machines"],
)

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


@router.get("", response_model=list[Machine])
async def list_machines() -> list[Machine]:
    """Return the current sample machines."""
    return machines


@router.get("/{machine_id}", response_model=Machine)
async def get_machine(machine_id: int = Path(gt=0)) -> Machine:
    """Return a machine by its ID."""
    for machine in machines:
        if machine.id == machine_id:
            return machine

    raise HTTPException(
        status_code=404,
        detail="Machine not found",
    )