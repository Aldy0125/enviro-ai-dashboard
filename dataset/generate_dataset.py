import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Total data rows
num_rows = 1000

# Start time
start_time = datetime(2026, 1, 1, 0, 0, 0)

# Generate timestamp every 10 minutes
timestamps = [start_time + timedelta(minutes=10 * i) for i in range(num_rows)]

# Set random seed so the result is consistent
np.random.seed(42)

# Generate realistic environmental sensor data
temperature = np.random.normal(loc=29, scale=2.5, size=num_rows)
humidity = np.random.normal(loc=70, scale=8, size=num_rows)
pm25 = np.random.normal(loc=35, scale=12, size=num_rows)
co2 = np.random.normal(loc=550, scale=100, size=num_rows)
light = np.random.normal(loc=450, scale=150, size=num_rows)
noise = np.random.normal(loc=55, scale=8, size=num_rows)

# Add artificial anomalies
anomaly_indices = np.random.choice(num_rows, size=50, replace=False)

temperature[anomaly_indices] += np.random.uniform(8, 15, size=50)
humidity[anomaly_indices] += np.random.uniform(15, 25, size=50)
pm25[anomaly_indices] += np.random.uniform(60, 120, size=50)
co2[anomaly_indices] += np.random.uniform(400, 800, size=50)
noise[anomaly_indices] += np.random.uniform(15, 30, size=50)

# Keep values in realistic range
temperature = np.clip(temperature, 20, 45)
humidity = np.clip(humidity, 35, 100)
pm25 = np.clip(pm25, 5, 180)
co2 = np.clip(co2, 350, 1500)
light = np.clip(light, 50, 1000)
noise = np.clip(noise, 30, 95)

# Generate environmental status
status = []

for i in range(num_rows):
    if pm25[i] > 100 or co2[i] > 1000 or temperature[i] > 38 or noise[i] > 80:
        status.append("Poor")
    elif pm25[i] > 50 or co2[i] > 800 or temperature[i] > 33 or noise[i] > 65:
        status.append("Moderate")
    else:
        status.append("Good")

# Create dataframe
df = pd.DataFrame({
    "timestamp": timestamps,
    "temperature": np.round(temperature, 2),
    "humidity": np.round(humidity, 2),
    "pm25": np.round(pm25, 2),
    "co2": np.round(co2, 2),
    "light": np.round(light, 2),
    "noise": np.round(noise, 2),
    "status": status
})

# Save dataset
df.to_csv("raw_data.csv", index=False)

print("Dataset created successfully: raw_data.csv")
print(df.head())
print("Total rows:", len(df))