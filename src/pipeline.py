import pandas as pd
import os

RAW_PATH = "data/raw/train.csv"
PROCESSED_PATH = "data/processed/cleaned_sales.csv"

def extract_data():
    print("Extracting data...")
    return pd.read_csv(RAW_PATH)

def transform_data(df):
    print("🔄 Transforming data...")

    # Cleaning column names
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    # Converting date
    df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce', dayfirst=True)

    # Feature engineering
    df['year'] = df['order_date'].dt.year
    df['month'] = df['order_date'].dt.month
    df['day'] = df['order_date'].dt.day
    df['week'] = df['order_date'].dt.isocalendar().week

    # Renaming for BI clarity
    df.rename(columns={'sales': 'revenue'}, inplace=True)

    # Droping missing values
    df.dropna(inplace=True)

    return df

def load_data(df):
    print("Loading data...")

    if os.path.exists(PROCESSED_PATH):
        print("Updating existing dataset (incremental simulation)...")
    else:
        print("Creating new dataset...")

    df.to_csv(PROCESSED_PATH, index=False)

def run_pipeline():
    df = extract_data()
    df = transform_data(df)
    load_data(df)
    print("✅ Pipeline completed!")

if __name__ == "__main__":
    run_pipeline()