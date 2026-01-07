import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path("data/raw")
PROCESSED_DATA_PATH = Path("data/processed")

def load_raw_data():
    file_path = RAW_DATA_PATH / "household_power_consumption.csv"
    df = pd.read_csv(
        file_path,
        sep=";",
        na_values=["?", "NA"],
        low_memory=False
    )
    return df

def basic_validation(df):
    print("Shape:", df.shape)
    print("Missing values:\n", df.isna().sum())
    print("Data types:\n", df.dtypes)

def save_processed(df):
    PROCESSED_DATA_PATH.mkdir(parents=True, exist_ok=True)
    output_path = PROCESSED_DATA_PATH / "energy_data_initial.csv"
    df.to_csv(output_path, index=False)
    print(f"Saved processed data to {output_path}")

if __name__ == "__main__":
    df = load_raw_data()
    basic_validation(df)
    save_processed(df)