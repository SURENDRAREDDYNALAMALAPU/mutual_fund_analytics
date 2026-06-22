import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../data/raw/hdfc_top100_clean.csv")

df["date"] = pd.to_datetime(df["date"])

plt.figure(figsize=(12,6))
plt.plot(df["date"], df["nav"])

plt.title("HDFC Top 100 Fund NAV Trend")
plt.xlabel("Date")
plt.ylabel("NAV")
plt.grid(True)

plt.savefig("../reports/nav_trend.png")

print("Chart saved successfully!")