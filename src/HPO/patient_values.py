from dataclasses import dataclass
from typing import Optional


@dataclass
class HPOPatientValues:
    """
    Standardized clinical observations for one patient.

    These are observed clinical values.
    They are NOT physiological model parameters.
    """

    patient_id: int

    # Demographics
    age: Optional[float] = None
    weight: Optional[float] = None
    height: Optional[float] = None
    bmi: Optional[float] = None

    # Hormonal observations
    fsh: Optional[float] = None
    lh: Optional[float] = None
    amh: Optional[float] = None
    progesterone: Optional[float] = None
    prolactin: Optional[float] = None
    tsh: Optional[float] = None

    # Derived hormonal observation
    fsh_lh_ratio: Optional[float] = None

    # Follicular observations
    follicle_count_left: Optional[float] = None
    follicle_count_right: Optional[float] = None
    total_follicle_count: Optional[float] = None

    follicle_size_left: Optional[float] = None
    follicle_size_right: Optional[float] = None
    mean_follicle_size: Optional[float] = None

    # Uterine observation
    endometrium: Optional[float] = None

    # Cycle observations
    cycle_regular: Optional[float] = None
    cycle_length_encoded: Optional[float] = None