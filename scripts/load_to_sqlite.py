import pandas as pd
import sqlite3

df = pd.read_csv("data/processed/hdfc_top100_clean.csv")

conn = sqlite3.connect("bluestock_mf.db")

df.to_sql("fact_nav", conn, if_exists="replace", index=False)

print("Database created successfully!")

conn.close()