# Enviro AI Dashboard

AI-Based Interactive Dashboard for Environmental Monitoring Using Anomaly Detection.

## Project Description

This project is developed for the Interactive Visualization Technique course. The system visualizes environmental monitoring data and applies an AI/ML method to detect abnormal environmental conditions.

The dashboard is designed to help users understand environmental changes through interactive charts, summary cards, anomaly detection results, and data insights.

## Project Title

AI-Based Interactive Dashboard for Environmental Monitoring Using Anomaly Detection

## Main Features

- Environmental time-series dataset
- Data preprocessing
- Anomaly detection using AI/ML
- Backend API
- Interactive dashboard
- Summary statistics
- Anomaly visualization
- Scientific paper using IMRaD format

## Dataset Variables

The dataset contains environmental monitoring variables, including:

- Timestamp
- Temperature
- Humidity
- PM2.5
- CO2
- Light intensity
- Noise level
- Environmental status

## AI/ML Method

This project uses an anomaly detection method to identify abnormal environmental conditions from sensor data. The model analyzes multiple variables such as temperature, humidity, PM2.5, CO2, light intensity, and noise level.

The output of the AI/ML process is used to classify data points as normal or anomalous.

## Project Structure

```text
enviro-ai-dashboard/
├── dataset/
├── backend/
├── frontend/
├── ai_model/
├── paper/
├── presentation/
├── README.md
└── .gitignore
```

## Folder Description

```text
dataset/       Stores raw and cleaned environmental datasets
backend/       Stores backend API source code
frontend/      Stores dashboard frontend source code
ai_model/      Stores AI/ML training code and model output
paper/         Stores final scientific paper files
presentation/  Stores final presentation files
```

## Planned API Endpoints

```text
/api/data/raw        Get raw environmental data
/api/data/clean      Get cleaned environmental data
/api/summary         Get summary statistics
/api/anomaly         Get anomaly detection results
/api/visualization   Get prepared data for dashboard visualization
```

## Author

Aldy Putra Manurung