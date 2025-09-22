import pandas as pd

# Load dataset
df = pd.read_csv("marketing_campaign.csv", sep="\t")

# 1. Handle missing Income (fill with median)
df['Income'] = df['Income'].fillna(df['Income'].median())

# 2. Convert Dt_Customer to datetime
df['Dt_Customer'] = pd.to_datetime(df['Dt_Customer'], errors='coerce')

# 3. Standardize Education categories
edu_map = {
    "2n Cycle": "Master",
    "Graduation": "Graduate",
    "PhD": "PhD",
    "Master": "Master",
    "Basic": "Basic"
}
df['Education'] = df['Education'].replace(edu_map)

# 4. Standardize Marital_Status categories
marital_map = {
    "Married": "Married",
    "Together": "Married",
    "Single": "Single",
    "Divorced": "Divorced",
    "Widow": "Widow",
    "Alone": "Single",
    "Absurd": "Single",
    "YOLO": "Single"
}
df['Marital_Status'] = df['Marital_Status'].replace(marital_map)

# 5. Remove unrealistic Year_Birth values
df = df[(df['Year_Birth'] >= 1900) & (df['Year_Birth'] <= 2022)]

# 6. Add Age column
current_year = pd.Timestamp.now().year
df['Age'] = current_year - df['Year_Birth']

# 7. Add Total Spend column
spend_cols = [
    'MntWines', 'MntFruits', 'MntMeatProducts',
    'MntFishProducts', 'MntSweetProducts', 'MntGoldProds'
]
df['TotalSpend'] = df[spend_cols].sum(axis=1)

# Save cleaned dataset
df.to_csv("cleaned_marketing_campaign.csv", index=False)

print("🎉 Cleaning complete! File saved as cleaned_marketing_campaign.csv")
