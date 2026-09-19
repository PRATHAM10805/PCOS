from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

from .config import TEST_SIZE, RANDOM_STATE


def prepare_data(X, y):

    # Stratified train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y
    )

    print("\nTrain/Test Split")
    print("----------------")
    print("Training:", X_train.shape)
    print("Testing :", X_test.shape)

    # Apply SMOTE only to training data
    smote = SMOTE(random_state=RANDOM_STATE)

    X_train_balanced, y_train_balanced = smote.fit_resample(
        X_train,
        y_train
    )

    print("\nClass distribution before SMOTE:")
    print(y_train.value_counts())

    print("\nClass distribution after SMOTE:")
    print(y_train_balanced.value_counts())

    return (
        X_train_balanced,
        X_test,
        y_train_balanced,
        y_test
    )