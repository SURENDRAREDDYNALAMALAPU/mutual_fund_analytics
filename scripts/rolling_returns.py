import pandas as pd

df = pd.read_csv("../data/raw/hdfc_top100_clean.csv")

df["date"] = pd.to_datetime(df["date"])

df["daily_return"] = df["nav"].pct_change() * 100

print(df[["date", "nav", "daily_return"]].head(10))

print("\nAverage Daily Return:")
print(df["daily_return"].mean())