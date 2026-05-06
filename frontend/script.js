const API_BASE_URL = "http://127.0.0.1:5000";

let visualizationData = [];
let tempHumidityChart;
let airQualityChart;
let anomalyChart;

async function fetchSummary() {
    try {
        const response = await fetch(`${API_BASE_URL}/api/summary`);
        const summary = await response.json();

        document.getElementById("totalData").textContent = summary.total_data;
        document.getElementById("totalNormal").textContent = summary.total_normal;
        document.getElementById("totalAnomaly").textContent = summary.total_anomaly;
        document.getElementById("avgTemperature").textContent = summary.average_temperature;
        document.getElementById("avgHumidity").textContent = summary.average_humidity;
        document.getElementById("avgPm25").textContent = summary.average_pm25;
        document.getElementById("avgCo2").textContent = summary.average_co2;
        document.getElementById("avgNoise").textContent = summary.average_noise;

        generateInsight(summary);
    } catch (error) {
        console.error("Failed to fetch summary:", error);
    }
}

async function fetchVisualizationData() {
    try {
        const response = await fetch(`${API_BASE_URL}/api/visualization`);
        visualizationData = await response.json();

        updateDashboard();
    } catch (error) {
        console.error("Failed to fetch visualization data:", error);
    }
}

function getLimitedData() {
    const limit = parseInt(document.getElementById("dataLimit").value);
    return visualizationData.slice(-limit);
}

function updateDashboard() {
    const data = getLimitedData();

    renderTempHumidityChart(data);
    renderAirQualityChart(data);
    renderAnomalyChart(data);
    renderTable(data);
}

function renderTempHumidityChart(data) {
    const labels = data.map(item => item.timestamp);
    const temperature = data.map(item => item.temperature);
    const humidity = data.map(item => item.humidity);

    if (tempHumidityChart) {
        tempHumidityChart.destroy();
    }

    const ctx = document.getElementById("tempHumidityChart");

    tempHumidityChart = new Chart(ctx, {
        type: "line",
        data: {
            labels: labels,
            datasets: [
                {
                    label: "Temperature (°C)",
                    data: temperature,
                    borderWidth: 2,
                    tension: 0.35
                },
                {
                    label: "Humidity (%)",
                    data: humidity,
                    borderWidth: 2,
                    tension: 0.35
                }
            ]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: "top"
                }
            },
            scales: {
                x: {
                    ticks: {
                        maxTicksLimit: 8
                    }
                }
            }
        }
    });
}

function renderAirQualityChart(data) {
    const labels = data.map(item => item.timestamp);
    const pm25 = data.map(item => item.pm25);
    const co2 = data.map(item => item.co2);

    if (airQualityChart) {
        airQualityChart.destroy();
    }

    const ctx = document.getElementById("airQualityChart");

    airQualityChart = new Chart(ctx, {
        type: "line",
        data: {
            labels: labels,
            datasets: [
                {
                    label: "PM2.5",
                    data: pm25,
                    borderWidth: 2,
                    tension: 0.35
                },
                {
                    label: "CO2 (ppm)",
                    data: co2,
                    borderWidth: 2,
                    tension: 0.35,
                    yAxisID: "y1"
                }
            ]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: "top"
                }
            },
            scales: {
                x: {
                    ticks: {
                        maxTicksLimit: 8
                    }
                },
                y: {
                    beginAtZero: true
                },
                y1: {
                    beginAtZero: true,
                    position: "right",
                    grid: {
                        drawOnChartArea: false
                    }
                }
            }
        }
    });
}

function renderAnomalyChart(data) {
    const labels = data.map(item => item.timestamp);
    const temperature = data.map(item => item.temperature);
    const anomalyPoints = data.map(item => {
        return item.anomaly_label === "Anomaly" ? item.temperature : null;
    });

    if (anomalyChart) {
        anomalyChart.destroy();
    }

    const ctx = document.getElementById("anomalyChart");

    anomalyChart = new Chart(ctx, {
        type: "line",
        data: {
            labels: labels,
            datasets: [
                {
                    label: "Temperature Trend",
                    data: temperature,
                    borderWidth: 2,
                    tension: 0.35
                },
                {
                    label: "Detected Anomaly",
                    data: anomalyPoints,
                    type: "scatter",
                    pointRadius: 6,
                    pointHoverRadius: 8,
                    showLine: false
                }
            ]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: "top"
                }
            },
            scales: {
                x: {
                    ticks: {
                        maxTicksLimit: 8
                    }
                }
            }
        }
    });
}

function renderTable(data) {
    const tableBody = document.getElementById("dataTable");
    tableBody.innerHTML = "";

    const latestData = data.slice(-20).reverse();

    latestData.forEach(item => {
        const row = document.createElement("tr");

        const anomalyBadge = item.anomaly_label === "Anomaly"
            ? `<span class="badge-anomaly">Anomaly</span>`
            : `<span class="badge-normal">Normal</span>`;

        row.innerHTML = `
            <td>${item.timestamp}</td>
            <td>${item.temperature}</td>
            <td>${item.humidity}</td>
            <td>${item.pm25}</td>
            <td>${item.co2}</td>
            <td>${item.noise}</td>
            <td>${item.environment_condition}</td>
            <td>${anomalyBadge}</td>
        `;

        tableBody.appendChild(row);
    });
}

function generateInsight(summary) {
    const anomalyPercentage = ((summary.total_anomaly / summary.total_data) * 100).toFixed(2);

    let conditionText = "";

    if (summary.average_pm25 > 75 || summary.average_co2 > 1000) {
        conditionText = "The environmental condition requires serious attention because the average air quality indicator is relatively high.";
    } else if (summary.average_pm25 > 35 || summary.average_co2 > 800) {
        conditionText = "The environmental condition is generally acceptable, but several indicators show moderate air quality levels.";
    } else {
        conditionText = "The environmental condition is generally good based on the average sensor readings.";
    }

    document.getElementById("insightText").textContent =
        `The system analyzed ${summary.total_data} environmental data records. ` +
        `A total of ${summary.total_anomaly} records were detected as anomalies, representing ${anomalyPercentage}% of the dataset. ` +
        `The average temperature is ${summary.average_temperature}°C, average humidity is ${summary.average_humidity}%, ` +
        `average PM2.5 is ${summary.average_pm25}, and average CO2 is ${summary.average_co2} ppm. ` +
        conditionText;
}

document.getElementById("dataLimit").addEventListener("change", updateDashboard);

fetchSummary();
fetchVisualizationData();