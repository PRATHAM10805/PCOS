from dataclasses import replace


def apply_scenario(
    patient_parameters,
    scenario,
):
    """
    Create a modified copy of the patient parameters.

    Scenario changes are stored in hpo_parameters until
    validated physiological mappings are implemented.
    """

    modified = replace(
        patient_parameters
    )

    existing_parameters = dict(
        modified.hpo_parameters or {}
    )

    existing_parameters.update(
        scenario
    )

    modified.hpo_parameters = (
        existing_parameters
    )

    return modified