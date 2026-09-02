import pandas as pd

titanic = pd.read_csv("titanic.csv")

print("Original Dataset:")
print(titanic.head())

titanic = titanic.drop_duplicates()

titanic["Age"] = titanic["Age"].fillna(titanic["Age"].mean())

titanic["Embarked"] = titanic["Embarked"].fillna(
    titanic["Embarked"].mode()[0]
)

titanic["Fare"] = titanic["Fare"].fillna(titanic["Fare"].median())

titanic["Age"] = pd.to_numeric(titanic["Age"], errors="coerce")

titanic["Fare"] = pd.to_numeric(titanic["Fare"], errors="coerce")

titanic = titanic.dropna(subset=["Age"])

print("\nCleaned Dataset:")
print(titanic.head())

print("\nDataset Information:")
print(titanic.info())