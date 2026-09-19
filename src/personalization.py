def create_patient_profile(patient_data, risk_probability):

    profile = {
        "risk_probability": risk_probability,
        "patient_parameters": patient_data
    }

    return profile


def prepare_simulation_input(patient_profile):

    """
    Placeholder for Phase 2.

    This module will eventually map patient-specific
    physiological parameters into the HPO-axis ODE model.
    """

    simulation_input = {
        "risk_probability": patient_profile["risk_probability"],
        "parameters": patient_profile["patient_parameters"]
    }

    return simulation_input