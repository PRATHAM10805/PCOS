from dataclasses import dataclass
from typing import Any

from src.HPO.model_runner import RoblitzModelRunner


@dataclass
class TwinScenario:
    name: str
    parameter_changes: dict[str, float]
    result: Any = None


class ScenarioSimulator:
    """
    Runs what-if simulations using the Röblitz model.

    Parameters may be supplied using either:
        - the Röblitz parameter name, e.g. b_syn_LH
        - the SBML parameter ID, e.g. p1
    """

    def __init__(self):
        self.runner = RoblitzModelRunner()

    def _resolve_parameter_id(self, model, parameter_name: str):
        """
        Resolve a Röblitz parameter name to its SBML parameter ID.
        """

        parameter_ids = list(
            model.getGlobalParameterIds()
        )

        # Allow direct SBML IDs such as p1.
        if parameter_name in parameter_ids:
            return parameter_name

        # Explicit mapping for parameters currently used by
        # the OvaTwin scenario layer.
        parameter_map = {
            "b_syn_LH": "p1",
        }

        if parameter_name in parameter_map:
            parameter_id = parameter_map[parameter_name]

            if parameter_id not in parameter_ids:
                raise ValueError(
                    f"SBML parameter ID {parameter_id} "
                    f"for {parameter_name} was not found."
                )

            return parameter_id

        raise ValueError(
            f"Unknown Röblitz model parameter: {parameter_name}"
        )

    def run(
        self,
        name: str,
        parameter_changes: dict[str, float],
        start_day: float = 0,
        end_day: float = 120,
        points: int = 1201,
    ) -> TwinScenario:

        # Always create an independent model for a scenario.
        model = self.runner.create_fresh_model()

        for parameter_name, value in parameter_changes.items():

            parameter_id = self._resolve_parameter_id(
                model,
                parameter_name,
            )

            model[parameter_id] = float(value)

        result = model.simulate(
            start_day,
            end_day,
            points,
        )

        return TwinScenario(
            name=name,
            parameter_changes=parameter_changes,
            result=result,
        )