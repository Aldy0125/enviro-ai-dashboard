# Enviro AI Dashboard

AI-Based Interactive Dashboard for Environmental Monitoring Using Anomaly Detection.

## Project Title

AI-Based Interactive Dashboard for Environmental Monitoring Using Anomaly Detection

## Author

Aldy Putra Manurung

## Project Description

Enviro AI Dashboard is an interactive environmental monitoring dashboard developed for the Interactive Visualization Technique course. This project visualizes environmental sensor data and applies an Artificial Intelligence/Machine Learning method to detect abnormal environmental conditions.

The system uses environmental time-series data containing temperature, humidity, PM2.5, CO2, light intensity, noise level, and environmental status. The data is processed through preprocessing, analyzed using anomaly detection, and displayed in an interactive web-based dashboard.

## Main Features

- Environmental time-series dataset
- Raw data and cleaned data
- Data preprocessing
- AI/ML-based anomaly detection
- Flask backend API
- Interactive frontend dashboard
- Summary statistic cards
- Time-series charts
- Anomaly visualization
- Latest environmental data table
- AI-generated insight text

## Dataset Variables

The dataset contains the following variables:

| Variable | Description |
|---|---|
| timestamp | Time record of sensor data |
| temperature | Environmental temperature in Celsius |
| humidity | Humidity percentage |
| pm25 | PM2.5 air quality value |
| co2 | CO2 concentration in ppm |
| light | Light intensity |
| noise | Noise level in dB |
| status | Environmental status category |
| date | Date extracted from timestamp |
| hour | Hour extracted from timestamp |
| air_quality | Air quality category based on PM2.5 |
| environment_condition | Environmental condition category |
| anomaly_label | AI/ML anomaly detection result |

## AI/ML Method

This project uses the Isolation Forest algorithm for anomaly detection.

Isolation Forest is selected because it is suitable for detecting unusual patterns in multivariate sensor data. The model analyzes several environmental variables, including:

- Temperature
- Humidity
- PM2.5
- CO2
- Light intensity
- Noise level

The output of the model classifies each data record into:

- Normal
- Anomaly

The anomaly detection result is then displayed in the dashboard through summary cards, charts, and data tables.

## Project Structure

```text
enviro-ai-dashboard/
├── dataset/
│   ├── generate_dataset.py
│   ├── preprocess_data.py
│   ├── raw_data.csv
│   └── clean_data.csv
│
├── ai_model/
│   ├── train_anomaly_model.py
│   ├── anomaly_result.csv
│   └── isolation_forest_model.pkl
│
├── backend/
│   └── app.py
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── paper/
├── presentation/
├── README.md
└── .gitignore
```

## Backend API Endpoints

| Endpoint | Description |
|---|---|
| `/` | Check API status |
| `/api/data/raw` | Get raw environmental dataset |
| `/api/data/clean` | Get cleaned environmental dataset |
| `/api/summary` | Get summary statistics |
| `/api/anomaly` | Get anomaly data only |
| `/api/visualization` | Get prepared data for dashboard visualization |

## How to Run the Project

### 1. Install Required Libraries

Run this command in the project root folder:

```bash
pip install pandas numpy scikit-learn joblib flask flask-cors
```

### 2. Generate Dataset

Go to the dataset folder:

```bash
cd dataset
```

Run the dataset generator:

```bash
python generate_dataset.py
```

This command will create:

```text
raw_data.csv
```

### 3. Preprocess Dataset

Still inside the dataset folder, run:

```bash
python preprocess_data.py
```

This command will create:

```text
clean_data.csv
```

### 4. Train Anomaly Detection Model

Go back to the project root folder:

```bash
cd ..
```

Go to the AI model folder:

```bash
cd ai_model
```

Run the model training script:

```bash
python train_anomaly_model.py
```

This command will create:

```text
anomaly_result.csv
isolation_forest_model.pkl
```

### 5. Run Backend API

Go back to the project root folder:

```bash
cd ..
```

Run the Flask backend:

```bash
python backend/app.py
```

The API will run at:

```text
http://127.0.0.1:5000
```

You can test the API using:

```text
http://127.0.0.1:5000/api/summary
```

### 6. Run Frontend Dashboard

Make sure the backend is still running.

Open the frontend file using Live Server:

```text
frontend/index.html
```

Or open it in the browser using:

```text
http://127.0.0.1:5500/frontend/index.html
```

## Dashboard Output

The dashboard displays:

- Total environmental data
- Total normal data
- Total anomaly data
- Average temperature
- Average humidity
- Average PM2.5
- Average CO2
- Average noise
- Temperature and humidity trend chart
- Air quality trend chart
- Anomaly detection visualization
- AI insight
- Latest environmental data table

## Current Result

Based on the generated dataset and anomaly detection result:

| Metric | Value |
|---|---:|
| Total Data | 1000 |
| Normal Data | 950 |
| Anomaly Data | 50 |
| Average Temperature | 29.61 °C |
| Average Humidity | 71.56 % |
| Average PM2.5 | 39.60 |
| Average CO2 | 578.93 ppm |

## Repository

GitHub Repository:

```text
https://github.com/Aldy0125/enviro-ai-dashboard
```