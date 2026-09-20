from typing import Any

from src.HPO.patient_values import HPOPatientValues


def _to_float(value: Any):
    if value is None:
        return None

    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def build_hpo_patient_values(row) -> HPOPatientValues:
    """
    Convert one cleaned clinical dataset row into
    standardized HPO patient observations.

    This function does NOT estimate physiological
    model parameters.
    """

    fsh = _to_float(row.get("FSH(mIU/mL)"))
    lh = _to_float(row.get("LH(mIU/mL)"))

    fsh_lh_ratio = None

    if fsh is not None and lh is not None and lh > 0:
        fsh_lh_ratio = fsh / lh

    left_follicles = _to_float(
        row.get("Follicle No. (L)")
    )

    right_follicles = _to_float(
        row.get("Follicle No. (R)")
    )

    total_follicles = None

    if (
        left_follicles is not None
        and right_follicles is not None
    ):
        total_follicles = (
            left_follicles
            + right_follicles
        )

    left_size = _to_float(
        row.get("Avg. F size (L) (mm)")
    )

    right_size = _to_float(
        row.get("Avg. F size (R) (mm)")
    )

    mean_size = None

    if (
        left_size is not None
        and right_size is not None
    ):
        mean_size = (
            left_size + right_size
        ) / 2

    patient_id = int(
        _to_float(
            row["Patient File No."]
        )
    )

    return HPOPatientValues(
        patient_id=patient_id,

        age=_to_float(
            row.get("Age (yrs)")
        ),

        weight=_to_float(
            row.get("Weight (Kg)")
        ),

        height=_to_float(
            row.get("Height(Cm)")
        ),

        bmi=_to_float(
            row.get("BMI")
        ),

        fsh=fsh,

        lh=lh,

        amh=_to_float(
            row.get("AMH(ng/mL)")
        ),

        progesterone=_to_float(
            row.get("PRG(ng/mL)")
        ),

        prolactin=_to_float(
            row.get("PRL(ng/mL)")
        ),

        tsh=_to_float(
            row.get("TSH (mIU/L)")
        ),

        fsh_lh_ratio=fsh_lh_ratio,

        follicle_count_left=left_follicles,

        follicle_count_right=right_follicles,

        total_follicle_count=total_follicles,

        follicle_size_left=left_size,

        follicle_size_right=right_size,

        mean_follicle_size=mean_size,

        endometrium=_to_float(
            row.get("Endometrium (mm)")
        ),

        cycle_regular=_to_float(
            row.get("Cycle(R/I)")
        ),

        cycle_length_encoded=_to_float(
            row.get("Cycle length(days)")
        ),
    )