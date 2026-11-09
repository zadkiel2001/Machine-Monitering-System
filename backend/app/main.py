import asyncio
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from typing import Literal
from fastapi import FastAPI
from pydantic import BaseModel
from app.reading_store import ReadingStore
from app.routes.machines import router as machines_router
from app.simulation_service import run_simulation
@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    store = ReadingStore()
    app.state.reading_store = store

    async with asyncio.TaskGroup() as tasks:
        simulation_task = tasks.create_task(run_simulation(store))

        try:
            yield
        finally:
            simulation_task.cancel()
app = FastAPI(
    title="PlantPulse API",
    description="Industrial machine monitoring API.",
    version="0.1.0",
    lifespan=lifespan,
)
app.include_router(machines_router)
class HealthResponse(BaseModel):
    """Public response contract for the API liveness check."""
    status: Literal["ok"]
@app.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check() -> HealthResponse:
    """Confirm that the API can respond to requests."""
    return HealthResponse(status="ok")