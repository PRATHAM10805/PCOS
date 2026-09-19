from xgboost import XGBClassifier

from .config import RANDOM_STATE


def train_model(X_train, y_train):

    model = XGBClassifier(
        n_estimators=200,
        max_depth=4,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=RANDOM_STATE,
        eval_metric="logloss"
    )

    model.fit(
        X_train,
        y_train
    )

    return model