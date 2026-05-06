import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os

# Path file
clean_data_path = "../dataset/clean_data.csv"
output_data_path = "anomaly_result.csv"
model_path = "isolation_forest_model.pkl"

# Read clean dataset
df = pd.read_csv(clean_data_path)

# Features used for anomaly detection
features = ["temperature", "humidity", "pm25", "co2", "light", "noise"]

X = df[features]

# Create Isolation Forest model
model = IsolationForest(
    n_estimators=100,
    contamination=0.05,
    random_state=42
)

# Train model and predict anomaly
df["anomaly_score"] = model.fit_predict(X)

# Convert result:
# 1 = Normal, -1 = Anomaly
df["anomaly_label"] = df["anomaly_score"].apply(
    lambda x: "Anomaly" if x == -1 else "Normal"
)

# Save result and model
df.to_csv(output_data_path, index=False)
joblib.dump(model, model_path)

# Summary
total_data = len(df)
total_anomaly = (df["anomaly_label"] == "Anomaly").sum()
total_normal = (df["anomaly_label"] == "Normal").sum()

print("Anomaly detection completed successfully.")
print("Result file created:", output_data_path)
print("Model file created:", model_path)
print("Total data:", total_data)
print("Normal data:", total_normal)
print("Anomaly data:", total_anomaly)
print(df[["timestamp", "temperature", "humidity", "pm25", "co2", "noise", "anomaly_label"]].head())