import pandas as pd

df = pd.read_csv("data.csv")

print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nDataset Information:")
print(df.info())