import pandas as pd
df = pd.read_csv("nutritionals.csv")
# print(df.columns.tolist())

columns_to_keep = [
    "food",
    "Caloric Value",
    "Fat",
    "Carbohydrates",
    "Protein",
    "Sugars",
    "Dietary Fiber",
    "Sodium",
    "Cholesterol",
    "Nutrition Density"   
]

df = df[columns_to_keep]

df.to_csv("cleaned.csv", index=False)