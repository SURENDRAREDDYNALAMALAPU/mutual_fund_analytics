import pandas as pd

df = pd.read_csv("../data/raw/hdfc_top100_clean.csv")

df["daily_return"] = df["nav"].pct_change()

volatility = df["daily_return"].std() * (252 ** 0.5) * 100

print(f"Annualized Volatility: {volatility:.2f}%")