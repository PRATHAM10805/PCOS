from dataclasses import dataclass, field
from typing import Any
from src.twin.scenarios import ScenarioSimulator
from src.HPO.baseline_simulation import run_baseline_simulation
from src.HPO.patient_values import HPOPatientValues
from src.twin.personalization import (
    PatientProfile,
    create_patient_profile,
)
from src.twin.parameter_mapping import PatientTwinMapping


@dataclass
class DigitalTwinState:
    baseline: Any = None
    scenarios: dict[str, Any] = field(default_factory=dict)


class PatientDigitalTwin:
    """
    Patient-specific digital twin.

    The twin combines:
    1. Clinical observations
    2. Patient-specific representation
    3. Röblitz HPO baseline simulation
    4. Future what-if simulations
    """

    def __init__(self, patient: HPOPatientValues):
        self.patient = patient
        self.scenario_simulator = ScenarioSimulator()
        self.profile: PatientProfile = create_patient_profile(patient)
        self.mapping: PatientTwinMapping = self.profile.mapping

        self.state = DigitalTwinState()

        self.ml_assessment = None

        self.status = "initialized"
    def compare_baseline_scenario(self, scenario_name: str):
        """
        Compare a stored scenario against the baseline simulation.

        Returns summary statistics for every common model variable.
        """

        if self.state.baseline is None:
            raise RuntimeError(
                "Baseline simulation must be run before comparison."
            )

        if scenario_name not in self.state.scenarios:
            raise ValueError(
                f"Scenario '{scenario_name}' does not exist."
            )

        baseline_result = self.state.baseline.result
        scenario_result = self.state.scenarios[scenario_name].result

        if baseline_result.shape != scenario_result.shape:
            raise ValueError(
                "Baseline and scenario trajectories have different shapes."
            )

        comparison = {}

        for column in baseline_result.colnames:
            if column == "time":
                continue

            baseline_values = baseline_result[column]
            scenario_values = scenario_result[column]

            difference = scenario_values - baseline_values

            comparison[column] = {
                "baseline_final": float(baseline_values[-1]),
                "scenario_final": float(scenario_values[-1]),
                "final_difference": float(difference[-1]),
                "maximum_absolute_difference": float(
                    max(abs(difference))
                ),
            }

        return comparison


        
    def get_status(self):
        return self.status
    
    def run_baseline(
        self,
        start_day: float = 0,
        end_day: float = 120,
        points: int = 1201,
    ):
        """
        Run the baseline Röblitz HPO simulation.

        At this stage, the simulation uses the published model's
        baseline parameterization. Patient observations remain
        separate and are not directly substituted into kinetic
        parameters without a validated mapping.
        """

        simulation = run_baseline_simulation(
            patient_id=self.patient.patient_id,
            start_day=start_day,
            end_day=end_day,
            points=points,
        )

        self.state.baseline = simulation
        self.status = "baseline_ready"

        return simulation

    def attach_ml_assessment(self, assessment):
        """
        Attach the ML-based PCOS assessment to the twin.
        """

        self.ml_assessment = assessment
        self.status = "ml_assessed"

    def add_scenario(self, name: str, simulation: Any):
        """
        Store a what-if simulation result.
        """

        self.state.scenarios[name] = simulation

    def summary(self):
        """
        Return a compact representation of the current twin state.
        """

        return {
            "patient_id": self.patient.patient_id,
            "status": self.status,
            "baseline_available": self.state.baseline is not None,
            "scenario_count": len(self.state.scenarios),
            "ml_assessment_available": self.ml_assessment is not None,
        }
    
    def run_scenario(
            self,
            name: str,
            parameter_changes: dict[str, float],
            start_day: float = 0,
            end_day: float = 120,
            points: int = 1201,
        ):
            """
            Run and store a patient-twin what-if scenario.
            """

            scenario = self.scenario_simulator.run(
                name=name,
                parameter_changes=parameter_changes,
                start_day=start_day,
                end_day=end_day,
                points=points,
            )

            self.state.scenarios[name] = scenario
            self.status = "scenario_ready"

            return scenario