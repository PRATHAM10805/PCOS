from dataclasses import fields

from .patient_values import HPOPatientValues


def validate_patient_values(
    patient: HPOPatientValues,
):
    """
    Check whether a patient has enough observations
    for downstream HPO personalization.

    This does not determine whether the patient has PCOS.
    """

    required_observations = [
        "fsh",
        "lh",
        "progesterone",
    ]

    missing = []

    for name in required_observations:
        value = getattr(patient, name)

        if value is None:
            missing.append(name)

    return {
        "patient_id": patient.patient_id,
        "valid": len(missing) == 0,
        "missing": missing,
    }