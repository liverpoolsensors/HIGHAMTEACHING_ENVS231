"""
make_data.py

Only hidden function for the ENVS231 practical.

Usage:
    datetime, dat1, dat2, dat3 = make_data(student_id)
"""

def make_data(student_id):
    import hashlib
    import numpy as np
    import pandas as pd

    # STAFF: replace this with the raw GitHub URL for the real data file
    data_url = "https://raw.githubusercontent.com/liverpoolsensors/HIGHAMTEACHING_ENVS231/refs/heads/main/data/data.csv"

    df = pd.read_csv(data_url)

    if "DateTime" in df.columns:
        datetime = np.array(pd.to_datetime(df["DateTime"], errors="coerce"))
    elif "tmp2" in df.columns:
        datetime = np.array(pd.to_datetime(df["tmp2"], errors="coerce"))
    else:
        datetime = np.array(pd.date_range("2021-01-01", periods=len(df), freq="h"))

    numeric_columns = []
    for col in df.columns:
        if col not in ["DateTime", "tmp2"]:
            if pd.api.types.is_numeric_dtype(df[col]):
                numeric_columns.append(col)

    if len(numeric_columns) < 3:
        raise ValueError("Need at least three numeric PM2.5 columns.")

    seed = int(hashlib.sha256(str(student_id).encode("utf-8")).hexdigest()[:8], 16)
    rng = np.random.default_rng(seed)

    chosen = rng.choice(numeric_columns, size=3, replace=False)

    dat1 = np.array(pd.to_numeric(df[chosen[0]], errors="coerce"))
    dat2 = np.array(pd.to_numeric(df[chosen[1]], errors="coerce"))
    dat3 = np.array(pd.to_numeric(df[chosen[2]], errors="coerce"))

    return datetime, dat1, dat2, dat3
