import numpy as np


class HPOSimulator:

    def __init__(self, model):
        self.model = model

    def simulate(
        self,
        days=120,
        step=0.1,
        initial_state=None,
        patient_parameters=None
    ):
        """
        Run the HPO-axis simulation.

        Parameters
        ----------
        days : float
            Simulation duration in days.

        step : float
            Integration step in days.

        initial_state : array-like, optional
            Initial physiological state.
        """

        if initial_state is None:
            initial_state = self.model.initial_state()

        times = np.arange(
            0,
            days + step,
            step
        )

        states = np.zeros(
            (len(times), len(initial_state))
        )

        states[0] = initial_state

        # The actual validated ODE integration will be added
        # once the physiological equations are incorporated.

        for i in range(1, len(times)):

            t = times[i - 1]
            current_state = states[i - 1]

            derivatives = self.model.derivatives(
                t,
                current_state
            )

            states[i] = (
                current_state
                + step * derivatives
            )

        return {
            "time": times,
            "states": states,
            "state_names": self.model.get_state_names(),
        }
