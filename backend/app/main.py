from typing import Literal

from fastapi import FastAPI
from pydantic import BaseModel

from app.routes.machines import router as machines_router


app = FastAPI(
    title="PlantPulse API",
    description="Industrial machine monitoring API.",
    version="0.1.0",
)

app.include_router(machines_router)


class HealthResponse(BaseModel):
    """Public response contract for the API liveness check."""

    status: Literal["ok"]


@app.get("/health", response_model=HealthResponse, tags=["Health"])
async def health_check() -> HealthResponse:
    """Confirm that the API can respond to requests."""
    return HealthResponse(status="ok")