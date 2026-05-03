import pandas as pd


def load_monthly_data(path: str) -> pd.DataFrame:
    """Load monthly Japan-to-Thailand visitor data."""
    df = pd.read_csv(path)
    df["date"] = pd.to_datetime(df["month"] + "-01")
    df = df.sort_values("date").reset_index(drop=True)
    return df


def add_time_series_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create lag, rolling, seasonality, and shock features."""
    df = df.copy()
    target_col = "japanese_visitors_to_thailand"

    df["month_number"] = df["date"].dt.month
    df["year"] = df["date"].dt.year

    for lag in [1, 2, 3, 12]:
        df[f"visitors_lag_{lag}"] = df[target_col].shift(lag)

    df["rolling_mean_3m"] = df[target_col].shift(1).rolling(3).mean()
    df["rolling_mean_6m"] = df[target_col].shift(1).rolling(6).mean()

    df["mom_growth_lag_1"] = df[target_col].pct_change(1).shift(1)
    df["yoy_growth_lag_1"] = df[target_col].pct_change(12).shift(1)

    # Transparent shock flag, not a magic deletion rule.
    df["shock_flag"] = 0
    df.loc[(df["date"] >= "2020-03-01") & (df["date"] <= "2022-09-01"), "shock_flag"] = 1

    # Statistical anomaly signal based on large drops.
    df["large_drop_flag"] = 0
    df.loc[(df[target_col].pct_change(12) <= -0.50) | (df[target_col].pct_change(1) <= -0.40), "large_drop_flag"] = 1

    return df


def add_targets(df: pd.DataFrame) -> pd.DataFrame:
    """Create next-month direction targets."""
    df = df.copy()
    target_col = "japanese_visitors_to_thailand"

    df["next_month_visitors"] = df[target_col].shift(-1)
    df["next_month_same_month_last_year"] = df[target_col].shift(11)

    df["target_mom_up"] = (df["next_month_visitors"] > df[target_col]).astype(int)
    df["target_yoy_up"] = (df["next_month_visitors"] > df["next_month_same_month_last_year"]).astype(int)

    return df


def build_modeling_table(path: str) -> pd.DataFrame:
    """Load data and return a model-ready table."""
    df = load_monthly_data(path)
    df = add_time_series_features(df)
    df = add_targets(df)
    df = df.dropna().reset_index(drop=True)
    return df
