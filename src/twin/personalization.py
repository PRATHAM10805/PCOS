from dataclasses import dataclass
from src.HPO.patient_values import HPOPatientValues


@dataclass
class PatientProfile:
    """
    Personalized computational profile of one patient.

    This contains observed patient information.
    It does not invent physiological parameters.
    """

    patient_id: int

    age: float | None
    weight: float | None
    height: float | None
    bmi: float | None

    fsh: float | None
    lh: float | None
    amh: float | None
    progesterone: float | None
    prolactin: float | None
    tsh: float | None

    fsh_lh_ratio: float | None

    total_follicle_count: float | None
    mean_follicle_size: float | None
    endometrium: float | None

    cycle_regular: float | None
    cycle_length_encoded: float | None


def create_patient_profile(
    patient: HPOPatientValues,
) -> PatientProfile:

    return PatientProfile(
        patient_id=patient.patient_id,

        age=patient.age,
        weight=patient.weight,
        height=patient.height,
        bmi=patient.bmi,

        fsh=patient.fsh,
        lh=patient.lh,
        amh=patient.amh,
        progesterone=patient.progesterone,
        prolactin=patient.prolactin,
        tsh=patient.tsh,

        fsh_lh_ratio=patient.fsh_lh_ratio,

        total_follicle_count=patient.total_follicle_count,
        mean_follicle_size=patient.mean_follicle_size,
        endometrium=patient.endometrium,

        cycle_regular=patient.cycle_regular,
        cycle_length_encoded=patient.cycle_length_encoded,
    )