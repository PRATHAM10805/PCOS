from dataclasses import dataclass

from src.HPO.patient_values import HPOPatientValues
from src.twin.parameter_mapping import PatientTwinMapping, create_mapping


@dataclass
class PatientProfile:
    patient: HPOPatientValues
    mapping: PatientTwinMapping


def create_patient_profile(patient: HPOPatientValues) -> PatientProfile:
    """
    Create the patient-specific representation used by OvaTwin.
    """

    mapping = create_mapping(patient)

    return PatientProfile(
        patient=patient,
        mapping=mapping,
    )