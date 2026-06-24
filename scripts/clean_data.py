import pandas as pd

df = pd.read_csv("../data/raw/hdfc_top100_nav.csv")

df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")
df = df.drop_duplicates()
df = df[df["nav"] > 0]

df.to_csv(
    "../data/processed/hdfc_top100_nav_cleaned.csv",
    index=False
)

print("Cleaning completed successfully!")

