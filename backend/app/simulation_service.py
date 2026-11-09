import asyncio
from random import Random
from app.reading_store import ReadingStore
from app.sample_data import machines
from app.simulator import generate_reading
INTERVAL_SECONDS = 2.0
async def run_simulation(store: ReadingStore) -> None:
    """Continuously update the latest reading for every machine."""
    rng = Random()
    while True:
        for machine in machines:
            reading = generate_reading(machine, rng)
            store.save(reading)
        await asyncio.sleep(INTERVAL_SECONDS)