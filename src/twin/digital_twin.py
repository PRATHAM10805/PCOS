from dataclasses import dataclass, field
from typing import Any, Optional

from src.HPO.patient_values import HPOPatientValues
from src.HPO.parameters import HPOParameters
from src.twin.parameter_mapping import create_mapping
from src.twin.personalization import (
    create_patient_profile,
)

@dataclass
class DigitalTwinState:
    """
    Current computational state of a patient's digital twin.

    The physiological state will be populated once a validated
    HPO model is connected.
    """

    baseline: Optional[Any] = None

    scenarios: dict[str, Any] = field(
        default_factory=dict
    )


class PatientDigitalTwin:
    """
    Computational representation of one patient.

    The twin combines:
        1. Patient observations
        2. Personalized model parameters
        3. Physiological model state
        4. Scenario states

    The HPO simulation is intentionally not executed until
    a validated physiological model is connected.
    """

    def __init__(
        self,
        patient: HPOPatientValues,
    ):
        self.patient = patient

        self.profile = create_patient_profile(
        patient
        )
        
        self.mapping = create_mapping(
            patient
        )

        self.parameters: HPOParameters = (
            self.mapping["parameters"]
        )

        self.state = DigitalTwinState()

        self.hpo_model = None

    # ---------------------------------------------------------
    # Model connection
    # ---------------------------------------------------------

    def attach_hpo_model(self, model):
        """
        Attach a validated HPO model to the twin.
        """

        self.hpo_model = model

    # ---------------------------------------------------------
    # Status
    # ---------------------------------------------------------

    def get_status(self):
        """
        Return the current readiness status of the twin.
        """

        return {
            "patient_id": self.patient.patient_id,

            "observations_available": (
                self.patient is not None
            ),

            "parameters_available": (
                self.parameters is not None
            ),

            "hpo_model_available": (
                self.hpo_model is not None
            ),

            "baseline_simulation_available": (
                self.state.baseline is not None
            ),

            "scenario_count": len(
                self.state.scenarios
            ),
        }

    # ---------------------------------------------------------
    # Baseline simulation
    # ---------------------------------------------------------

    def simulate_baseline(
        self,
        *args,
        **kwargs,
    ):
        """
        Run the baseline physiological simulation.

        This method remains unavailable until an HPO model
        has been attached.
        """

        if self.hpo_model is None:
            raise RuntimeError(
                "No HPO model is attached to the "
                "digital twin."
            )

        result = self.hpo_model.simulate(
            patient=self.patient,
            parameters=self.parameters,
            *args,
            **kwargs,
        )

        self.state.baseline = result

        return result

    # ---------------------------------------------------------
    # Scenario
    # ---------------------------------------------------------

    def add_scenario(
        self,
        name: str,
        scenario_state: Any,
    ):
        """
        Store a simulated scenario state.
        """

        self.state.scenarios[name] = (
            scenario_state
        )

    # ---------------------------------------------------------
    # Twin summary
    # ---------------------------------------------------------

    def summary(self):
        """
        Return a compact representation of the twin.
        """

        return {
            "patient_id": self.patient.patient_id,

            "observations": {
                "FSH": self.patient.fsh,
                "LH": self.patient.lh,
                "AMH": self.patient.amh,
                "Progesterone": (
                    self.patient.progesterone
                ),
                "Follicle count": (
                    self.patient.total_follicle_count
                ),
                "Mean follicle size": (
                    self.patient.mean_follicle_size
                ),
                "Endometrium": (
                    self.patient.endometrium
                ),
            },

            "hpo_model_attached": (
                self.hpo_model is not None
            ),

            "baseline_available": (
                self.state.baseline is not None
            ),

            "scenario_count": len(
                self.state.scenarios
            ),
        }