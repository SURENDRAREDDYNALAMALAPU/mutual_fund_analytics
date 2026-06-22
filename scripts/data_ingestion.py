import pandas as pd
import os

folder = "../data/raw"

if not os.path.exists(folder):
    print("Raw data folder not found!")
else:
    files = os.listdir(folder)

    for file in files:
        if file.endswith(".csv"):
            path = os.path.join(folder, file)

            df = pd.read_csv(path)

            print("=" * 50)
            print("FILE:", file)
            print("SHAPE:", df.shape)

            print("\nDATA TYPES")
            print(df.dtypes)

            print("\nFIRST 5 ROWS")
            print(df.head())