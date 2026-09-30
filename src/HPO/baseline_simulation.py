from dataclasses import dataclass
from typing import Any

from src.HPO.model_runner import RoblitzModelRunner


@dataclass
class BaselineSimulation:
    patient_id: int
    start_day: float
    end_day: float
    points: int
    result: Any


def run_baseline_simulation(
    patient_id: int,
    start_day: float = 0,
    end_day: float = 120,
    points: int = 1201,
) -> BaselineSimulation:

    runner = RoblitzModelRunner()

    result = runner.simulate(
        start=start_day,
        end=end_day,
        points=points,
    )

    return BaselineSimulation(
        patient_id=patient_id,
        start_day=start_day,
        end_day=end_day,
        points=points,
        result=result,
    )