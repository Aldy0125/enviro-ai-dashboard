import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Jumlah data
num_rows = 1000

# Waktu mulai data
start_time = datetime(2026, 1, 1, 0, 0, 0)

# Membuat timestamp setiap 10 menit
timestamps = [start_time + timedelta(minutes=10 * i) for i in range(num_rows)]

# Membuat data sensor realistis
np.random.seed(42)

temperature = np.random.normal(loc=29, scale=2.5, size=num_rows)
humidity = np.random.normal(loc=70, scale=8, size=num_rows)
pm25 = np.random.normal(loc=35, scale=12, size=num_rows)
co2 = np.random.normal(loc=550, scale=100, size=num_rows)
light = np.random.normal(loc=450, scale=150, size=num_rows)
noise = np.random.normal(loc=55, scale=8, size=num_rows)

# Membuat beberapa data anomali secara sengaja
anomaly_indices = np.random.choice(num_rows, size=50, replace=False)

temperature[anomaly_indices] += np.random.uniform(8, 15, size=50)
humidity[anomaly_indices] += np.random.uniform(15, 25, size=50)
pm25[anomaly_indices] += np.random.uniform(60, 120, size=50)
co2[anomaly_indices] += np.random.uniform(400, 800, size=50)
noise[anomaly_indices] += np.random.uniform(15, 30, size=50)

# Membatasi nilai agar tetap realistis
temperature = np.clip(temperature, 20, 45)
humidity = np.clip(humidity, 35, 100)
pm25 = np.clip(pm25, 5, 180)
co2 = np.clip(co2, 350, 1500)
light = np.clip(light, 50, 1000)
noise = np.clip(noise, 30, 95)

# Membuat status kualitas lingkungan sederhana
status = []

for i in range(num_rows):
    if pm25[i] > 100 or co2[i] > 1000 or temperature[i] > 38 or noise[i] > 80:
        status.append("Poor")
    elif pm25[i] > 50 or co2[i] > 800 or temperature[i] > 33 or noise[i] > 65:
        status.append("Moderate")
    else:
        status.append("Good")

# Membuat dataframe
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

# Menyimpan data mentah
df.to_csv("raw_data.csv", index=False)

print("Dataset berhasil dibuat: raw_data.csv")
print(df.head())