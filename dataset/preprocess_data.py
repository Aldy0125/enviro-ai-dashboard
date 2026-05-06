import pandas as pd

# Read raw dataset
df = pd.read_csv("raw_data.csv")

# Convert timestamp to datetime format
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Numeric columns
numeric_columns = ["temperature", "humidity", "pm25", "co2", "light", "noise"]

# Fill missing values using mean value
for col in numeric_columns:
    df[col] = df[col].fillna(df[col].mean())

# Remove duplicate rows
df = df.drop_duplicates()

# Add date and hour columns for dashboard filtering
df["date"] = df["timestamp"].dt.date
df["hour"] = df["timestamp"].dt.hour

# Create air quality category based on PM2.5
def air_quality_category(pm25):
    if pm25 <= 35:
        return "Good"
    elif pm25 <= 75:
        return "Moderate"
    else:
        return "Poor"

df["air_quality"] = df["pm25"].apply(air_quality_category)

# Create environmental condition category
def environment_condition(row):
    if row["pm25"] > 100 or row["co2"] > 1000 or row["temperature"] > 38 or row["noise"] > 80:
        return "Unsafe"
    elif row["pm25"] > 50 or row["co2"] > 800 or row["temperature"] > 33 or row["noise"] > 65:
        return "Warning"
    else:
        return "Normal"

df["environment_condition"] = df.apply(environment_condition, axis=1)

# Round numeric data
for col in numeric_columns:
    df[col] = df[col].round(2)

# Save cleaned dataset
df.to_csv("clean_data.csv", index=False)

print("Preprocessing completed successfully.")
print("Clean dataset created: clean_data.csv")
print(df.head())
print("Total rows:", len(df))
print("\nMissing values:")
print(df.isnull().sum())