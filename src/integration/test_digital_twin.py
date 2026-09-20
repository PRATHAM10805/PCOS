import pandas as pd

from src.Clinical.hpo_observation_builder import (
    build_hpo_patient_values,
)

from src.twin.digital_twin import (
    PatientDigitalTwin,
)


DATA_PATH = "data/PCOS_data_without_infertility-Full_new.csv"


def main():

    df = pd.read_csv(DATA_PATH)

    patient = build_hpo_patient_values(
        df.iloc[0]
    )

    twin = PatientDigitalTwin(
        patient
    )

    print("\nDIGITAL TWIN")
    print("=" * 60)

    print("\nSTATUS")
    print("-" * 60)

    print(twin.get_status())

    print("\nSUMMARY")
    print("-" * 60)

    print(twin.summary())


if __name__ == "__main__":
    main()