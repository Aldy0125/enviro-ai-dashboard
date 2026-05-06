from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import os

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

RAW_DATA_PATH = os.path.join(BASE_DIR, "dataset", "raw_data.csv")
CLEAN_DATA_PATH = os.path.join(BASE_DIR, "dataset", "clean_data.csv")
ANOMALY_DATA_PATH = os.path.join(BASE_DIR, "ai_model", "anomaly_result.csv")


@app.route("/")
def home():
    return jsonify({
        "message": "Enviro AI Dashboard API is running",
        "available_endpoints": [
            "/api/data/raw",
            "/api/data/clean",
            "/api/summary",
            "/api/anomaly",
            "/api/visualization"
        ]
    })


@app.route("/api/data/raw")
def get_raw_data():
    df = pd.read_csv(RAW_DATA_PATH)
    return jsonify(df.to_dict(orient="records"))


@app.route("/api/data/clean")
def get_clean_data():
    df = pd.read_csv(CLEAN_DATA_PATH)
    return jsonify(df.to_dict(orient="records"))


@app.route("/api/summary")
def get_summary():
    df = pd.read_csv(ANOMALY_DATA_PATH)

    total_data = len(df)
    total_normal = len(df[df["anomaly_label"] == "Normal"])
    total_anomaly = len(df[df["anomaly_label"] == "Anomaly"])

    summary = {
        "total_data": total_data,
        "total_normal": total_normal,
        "total_anomaly": total_anomaly,
        "average_temperature": round(df["temperature"].mean(), 2),
        "average_humidity": round(df["humidity"].mean(), 2),
        "average_pm25": round(df["pm25"].mean(), 2),
        "average_co2": round(df["co2"].mean(), 2),
        "average_noise": round(df["noise"].mean(), 2),
        "max_temperature": round(df["temperature"].max(), 2),
        "max_pm25": round(df["pm25"].max(), 2),
        "max_co2": round(df["co2"].max(), 2)
    }

    return jsonify(summary)


@app.route("/api/anomaly")
def get_anomaly_data():
    df = pd.read_csv(ANOMALY_DATA_PATH)
    anomaly_df = df[df["anomaly_label"] == "Anomaly"]
    return jsonify(anomaly_df.to_dict(orient="records"))


@app.route("/api/visualization")
def get_visualization_data():
    df = pd.read_csv(ANOMALY_DATA_PATH)

    selected_columns = [
        "timestamp",
        "temperature",
        "humidity",
        "pm25",
        "co2",
        "light",
        "noise",
        "status",
        "air_quality",
        "environment_condition",
        "anomaly_label"
    ]

    df = df[selected_columns]

    return jsonify(df.to_dict(orient="records"))


if __name__ == "__main__":
    app.run(debug=True)