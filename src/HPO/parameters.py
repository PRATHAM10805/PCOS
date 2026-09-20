from dataclasses import dataclass
from typing import Optional


@dataclass
class HPOParameters:
    """
    Physiological model parameters.

    Values remain None until they are obtained from the
    selected HPO model or a documented calibration procedure.
    """

    # Core axis
    gnrh_production: Optional[float] = None
    gnrh_clearance: Optional[float] = None

    fsh_production: Optional[float] = None
    fsh_clearance: Optional[float] = None

    lh_production: Optional[float] = None
    lh_clearance: Optional[float] = None

    # Ovarian hormones
    estradiol_production: Optional[float] = None
    estradiol_clearance: Optional[float] = None

    progesterone_production: Optional[float] = None
    progesterone_clearance: Optional[float] = None

    # Inhibins
    inhibin_a_production: Optional[float] = None
    inhibin_a_clearance: Optional[float] = None

    inhibin_b_production: Optional[float] = None
    inhibin_b_clearance: Optional[float] = None

    # Feedback
    fsh_feedback: Optional[float] = None
    lh_feedback: Optional[float] = None

    estradiol_feedback: Optional[float] = None
    progesterone_feedback: Optional[float] = None

    # Follicular dynamics
    follicular_growth_rate: Optional[float] = None
    follicular_atresia_rate: Optional[float] = None

    # Patient-specific modifiers
    amh_modifier: Optional[float] = None
    metabolic_modifier: Optional[float] = None
    cycle_modifier: Optional[float] = None