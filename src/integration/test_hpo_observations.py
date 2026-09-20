import pandas as pd

from src.Clinical.hpo_observation_builder import (
    build_hpo_patient_values,
)

from src.HPO.validation import (
    validate_patient_values,
)


DATA_PATH = "data/PCOS_data_without_infertility-Full_new.csv"


def main():

    df = pd.read_csv(DATA_PATH)

    row = df.iloc[0]

    patient = build_hpo_patient_values(row)

    print("\nPATIENT OBSERVATIONS")
    print("=" * 50)
    print(patient)

    validation = validate_patient_values(
        patient
    )

    print("\nVALIDATION")
    print("=" * 50)
    print(validation)


if __name__ == "__main__":
    main()