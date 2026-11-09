from random import Random
from time import sleep
from app.sample_data import machines
from app.simulator import generate_reading
INTERVAL_SECONDS = 2.0
def main() -> None:
    rng = Random()
    print("PlantPulse simulator started. Press Ctrl+C to stop.")
    try:
        while True:
            for machine in machines:
                reading = generate_reading(machine, rng)
                print(reading.model_dump_json(), flush=True)
            sleep(INTERVAL_SECONDS)
    except KeyboardInterrupt:
        print("\nSimulator stopped.")
if __name__ == "__main__":
    main()