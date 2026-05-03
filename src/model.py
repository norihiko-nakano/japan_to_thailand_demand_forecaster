from pathlib import Path

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from features import build_modeling_table


DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "sample_jttd_monthly.csv"


FEATURES = [
    "visitors_lag_1",
    "visitors_lag_2",
    "visitors_lag_3",
    "visitors_lag_12",
    "rolling_mean_3m",
    "rolling_mean_6m",
    "mom_growth_lag_1",
    "yoy_growth_lag_1",
    "month_number",
    "public_holiday_count_japan",
    "is_golden_week_month",
    "is_obon_month",
    "is_new_year_travel_month",
    "jpy_thb_exchange_rate_proxy",
    "shock_flag",
    "large_drop_flag",
]


def time_based_split(df: pd.DataFrame, train_end: str = "2023-12-01"):
    """Split chronologically to avoid future leakage."""
    train = df[df["date"] <= train_end].copy()
    test = df[df["date"] > train_end].copy()
    return train, test


def train_and_evaluate(target: str = "target_yoy_up") -> None:
    df = build_modeling_table(str(DATA_PATH))
    train, test = time_based_split(df)

    X_train = train[FEATURES]
    y_train = train[target]
    X_test = test[FEATURES]
    y_test = test[target]

    models = {
        "logistic_regression": Pipeline([
            ("scaler", StandardScaler()),
            ("model", LogisticRegression(max_iter=1000))
        ]),
        "random_forest": RandomForestClassifier(
            n_estimators=200,
            random_state=42,
            min_samples_leaf=3
        ),
    }

    print(f"\nTarget: {target}")
    print("=" * 60)

    for name, model in models.items():
        model.fit(X_train, y_train)
        pred = model.predict(X_test)

        print(f"\nModel: {name}")
        print(f"Accuracy: {accuracy_score(y_test, pred):.3f}")
        print("Confusion matrix:")
        print(confusion_matrix(y_test, pred))
        print("Classification report:")
        print(classification_report(y_test, pred, zero_division=0))

    latest = df.iloc[[-1]][FEATURES]
    chosen_model = models["random_forest"]
    chosen_model.fit(df[FEATURES], df[target])
    prediction = chosen_model.predict(latest)[0]
    probability = chosen_model.predict_proba(latest)[0][prediction]

    label = "increase" if prediction == 1 else "decrease"
    print("\nLatest sample forecast")
    print("-" * 60)
    print(f"Predicted next-month direction: {label}")
    print(f"Confidence proxy: {probability:.2%}")
    print("\nSuggested business action:")
    if prediction == 1:
        print("- Increase Thailand visibility on Japanese-language travel pages.")
        print("- Prepare Thailand campaign content for the next travel planning window.")
    else:
        print("- Keep Thailand exposure stable and monitor new demand signals.")
        print("- Avoid over-allocating campaign space until demand improves.")


if __name__ == "__main__":
    train_and_evaluate("target_yoy_up")
    train_and_evaluate("target_mom_up")
