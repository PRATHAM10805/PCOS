from src.HPO.parameters import HPOParameters
from src.HPO.patient_values import HPOPatientValues


def create_mapping(
    patient: HPOPatientValues,
):
    """
    Prepare a patient's observations for future
    HPO-model calibration.

    No unsupported physiological parameter conversion
    is performed.
    """

    parameters = HPOParameters()

    return {
        "patient_id": patient.patient_id,

        "observations": {
            "FSH": patient.fsh,
            "LH": patient.lh,
            "AMH": patient.amh,
            "Progesterone": patient.progesterone,
            "Prolactin": patient.prolactin,
            "TSH": patient.tsh,
        },

        "follicular_observations": {
            "left_count": patient.follicle_count_left,
            "right_count": patient.follicle_count_right,
            "total_count": patient.total_follicle_count,
            "left_size": patient.follicle_size_left,
            "right_size": patient.follicle_size_right,
            "mean_size": patient.mean_follicle_size,
        },

        "uterine_observations": {
            "endometrium": patient.endometrium,
        },

        "cycle_observations": {
            "cycle_regular": patient.cycle_regular,
            "cycle_length_encoded": (
                patient.cycle_length_encoded
            ),
        },

        "parameters": parameters,

        "status": "awaiting_hpo_model",
    }