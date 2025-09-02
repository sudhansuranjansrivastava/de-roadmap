import pandas as pd
from pathlib import Path

raw_path = Path("data/raw/sales.csv")

# Read CSV
df = pd.read_csv(raw_path)

# Clean types
df["date"] = pd.to_datetime(df["date"], errors="coerce")
df["qty"] = pd.to_numeric(df["qty"], errors="coerce").fillna(0).astype(int)
df["price"] = pd.to_numeric(df["price"], errors="coerce").fillna(0.0)

# Feature: revenue
df["revenue"] = df["qty"] * df["price"]

# Show first 5 rows
print(df.head().to_string(index=False))
