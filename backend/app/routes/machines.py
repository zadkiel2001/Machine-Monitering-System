from fastapi import APIRouter, HTTPException, Path
from app.schemas import Machine
from app.sample_data import machines
router = APIRouter(
    prefix="/machines",
    tags=["Machines"],
)
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