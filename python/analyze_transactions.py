
import pandas as pd
from pathlib import Path

# Locate the project dataset
DATA_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "telangana_rice_mill_transactions_100k (1).csv"
)

# Load the dataset
df = pd.read_csv(DATA_FILE)

# Display basic dataset information
print("TELANGANA RICE MILL TRANSACTION ANALYTICS")
print("=" * 45)

print(f"\nTotal records: {len(df):,}")
print(f"Total columns: {len(df.columns)}")

print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst five records:")
print(df.head())

print("\nMissing values in each column:")
print(df.isnull().sum())

print("\nDataset summary:")
print(df.describe(include="all").to_string())
