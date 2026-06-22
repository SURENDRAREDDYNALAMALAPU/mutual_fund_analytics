import pandas as pd

df = pd.read_csv("../data/raw/hdfc_top100_clean.csv")

start_nav = df.iloc[0]["nav"]
end_nav = df.iloc[-1]["nav"]

years = (pd.to_datetime(df.iloc[-1]["date"]) -
         pd.to_datetime(df.iloc[0]["date"])).days / 365

cagr = ((end_nav / start_nav) ** (1 / years) - 1) * 100

print(f"Start NAV: {start_nav:.2f}")
print(f"End NAV: {end_nav:.2f}")
print(f"Years: {years:.2f}")
print(f"CAGR: {cagr:.2f}%")