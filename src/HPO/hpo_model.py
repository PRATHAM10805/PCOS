from dataclasses import dataclass
import numpy as np


@dataclass
class HPOState:
    """
    Core hormonal state exposed by the simulation.

    The full Röblitz/GynCycle model contains additional internal
    biological states. These core variables are used by OvaTwin
    for visualization and downstream analysis.
    """

    gnrh: float
    fsh: float
    lh: float
    estradiol: float
    progesterone: float
    inhibin_a: float
    inhibin_b: float


class HPOModel:
    """
    HPO-axis simulation interface.

    The implementation is intentionally separated from the patient
    personalization layer so that the validated physiological
    equations and parameters can be inserted without changing the
    rest of the OvaTwin architecture.
    """

    def __init__(self, parameters=None):
        self.parameters = parameters or {}

    def initial_state(self):
        """
        Return initial physiological state.

        Values here are normalized state variables for the simulation
        interface, not clinical hormone measurements.
        """

        return np.array([
            1.0,  # GnRH
            1.0,  # FSH
            1.0,  # LH
            1.0,  # Estradiol
            1.0,  # Progesterone
            1.0,  # Inhibin A
            1.0,  # Inhibin B
        ], dtype=float)

    def derivatives(self, t, state):
        """
        Placeholder for the validated HPO differential equations.

        This method will contain the Röblitz equations once the
        corresponding parameter/state definitions are incorporated.
        """

        raise NotImplementedError(
            "Validated HPO-axis equations have not yet been inserted."
        )

    def get_state_names(self):
        return [
            "GnRH",
            "FSH",
            "LH",
            "Estradiol",
            "Progesterone",
            "Inhibin A",
            "Inhibin B",
        ]