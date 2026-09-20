from sklearn.feature_selection import SelectKBest, mutual_info_classif


def select_features(X_train, y_train, X_test, k=15):

    k = min(k, X_train.shape[1])

    selector = SelectKBest(
        score_func=mutual_info_classif,
        k=k
    )

    X_train_selected = selector.fit_transform(
        X_train,
        y_train
    )

    X_test_selected = selector.transform(X_test)

    selected_features = X_train.columns[
        selector.get_support()
    ].tolist()

    X_train_selected = X_train[
        selected_features
    ]

    X_test_selected = X_test[
        selected_features
    ]

    print("\nSelected Features:")

    for feature in selected_features:
        print("-", feature)

    return (
        X_train_selected,
        X_test_selected,
        selected_features,
        selector
    )