import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("data/raw/players_data_light-2025_2026.csv")

print(df.shape)
print(df.columns.tolist())
print(df.head())

#removing goalkeepers (maintaing outfield player model)
df = df[~df["Pos"].str.contains("GK", na=False)]

print("After removing goalkeepers:", df.shape)
print(df["Pos"].value_counts())

df = df[df["Min"] >= 900]
print("After 900-minute filter:", df.shape)
print(df["Min"].describe())

print("\nMissing values by column:")
print(df.isna().sum().sort_values(ascending=False))

#dropping nonOutfield columns
drop_cols = [
    "PKm", "PKsv", "PKA", "PKatt_stats_keeper",
    "CS%", "CS", "L", "D", "W",
    "Save%", "Saves", "SoTA", "GA90", "GA"
]

df = df.drop(columns=drop_cols)
print("\nAfter dropping goalkeeper-only columns", df.shape)

#dropping players w/ 0 shots or 0 SoT
df = df.dropna(subset=["G/SoT", "SoT%", "G/Sh"])
print("After dropping rows with missing shooting-rate stats:", df.shape)
print("\nRemaining missing values:")
print(df.isna().sum().sort_values(ascending=False))

keep_cols = [
    "Player", "Nation", "Pos", "Squad", "Comp", "Age", "Born",
    "MP", "Starts", "Min", "90s",
    "Gls", "Ast", "G+A", "G-PK", "PK", "PKatt",
    "Sh", "SoT", "SoT%", "Sh/90", "SoT/90", "G/Sh", "G/SoT",
    "CrdY", "CrdR", "Fld", "Fls", "Crs", "OG",
    "TklW", "Int", "2CrdY"
]

df = df[keep_cols]

print("\nAfter keeping selected modeling columns:", df.shape)
print(df.head())

df.to_csv("data/processed/players_cleaned.csv", index=False)
print("\nSaved cleaned modeling dataset to data/processed/players_cleaned.csv")

index_cols = ["Gls", "Ast", "SoT/90", "G/Sh", "TklW", "Int", "Fld"]

scaler = StandardScaler()
scaled_values = scaler.fit_transform(df[index_cols])

scaled_df = pd.DataFrame(
    scaled_values,
    columns=[col + "_z" for col in index_cols]
)

#z-score columns
df = pd.concat([df.reset_index(drop=True), scaled_df], axis=1)

#composite performance index
df["performance_index"] = (
    df["Gls_z"] + df["Ast_z"] + df["SoT/90_z"] +
    df["G/Sh_z"] + df["TklW_z"] + df["Int_z"] +
    df["Fld_z"]
) / 7

print("\nPerformance index summary:")
print(df["performance_index"].describe())

#save new dataset
df.to_csv("data/processed/players_performance_index.csv", index=False)
print("\nSaved dataset with performance index to data/processed/players_performance_index.csv")
