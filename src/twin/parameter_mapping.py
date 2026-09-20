from dataclasses import dataclass, field

from src.HPO.patient_values import HPOPatientValues


@dataclass
class PatientTwinMapping:
    """
    Patient-specific observations used by the digital twin.

    These values are observations from the clinical dataset.
    They are kept separate from the fixed kinetic parameters
    of the Röblitz HPO model.
    """

    patient_id: int

    hormones: dict[str, float | None] = field(default_factory=dict)
    follicular: dict[str, float | None] = field(default_factory=dict)
    uterine: dict[str, float | None] = field(default_factory=dict)
    cycle: dict[str, float | None] = field(default_factory=dict)
    anthropometric: dict[str, float | None] = field(default_factory=dict)


def create_mapping(patient: HPOPatientValues) -> PatientTwinMapping:
    """
    Convert clinical/HPO observations into the patient-specific
    representation used by the digital twin.

    Important:
    These observations are NOT automatically written into
    Röblitz kinetic parameters.
    """

    return PatientTwinMapping(
        patient_id=patient.patient_id,

        hormones={
            "FSH": patient.fsh,
            "LH": patient.lh,
            "AMH": patient.amh,
            "Progesterone": patient.progesterone,
            "Prolactin": patient.prolactin,
            "TSH": patient.tsh,
            "FSH_LH_ratio": patient.fsh_lh_ratio,
        },

        follicular={
            "left_count": patient.follicle_count_left,
            "right_count": patient.follicle_count_right,
            "total_count": patient.total_follicle_count,
            "left_size": patient.follicle_size_left,
            "right_size": patient.follicle_size_right,
            "mean_size": patient.mean_follicle_size,
        },

        uterine={
            "endometrium": patient.endometrium,
        },

        cycle={
            "regular": patient.cycle_regular,
            "length_encoded": patient.cycle_length_encoded,
        },

        anthropometric={
            "age": patient.age,
            "weight": patient.weight,
            "height": patient.height,
            "bmi": patient.bmi,
        },
    )