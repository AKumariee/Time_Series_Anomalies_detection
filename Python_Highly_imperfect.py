import random
import csv

# Define time range
start_date = "2019-01-01 00:00:00"
end_date = "2022-01-01 00:00:00"

# Define data frequency (minutes)
frequency = 15

# Define features and their data types
features = {
    "Timestamp": str,
    "Pressure (inlet)": float,
    "Temperature (inlet)": float,
    "Pressure (outlet)": float,
    "Temperature (outlet)": float,
    "Flow Rate": float,
    "Vibration (x-axis)": float,
    "Vibration (y-axis)": float,
    "Vibration (z-axis)": float,
    "Alert (on/off)": str,
    "Alert Code": str,
    "Power Consumption": float,
    "Humidity Level (%)": float,
    "Gas Concentration (ppm)": float,
    "Anomalies Flag": str,
}

# Function to generate random sensor readings within a range
def generate_sensor_reading(base_value, variation):
    return round(base_value + random.uniform(-variation, variation), 2)

# Function to simulate random anomaly events
def generate_anomaly(datapoint):
    anomaly_type = random.choice(["pressure_spike", "temperature_drop", "flow_decrease", "gas_concentration_surge"])
    if anomaly_type == "pressure_spike":
        datapoint["Pressure (inlet)"] *= 1.5
        datapoint["Pressure (outlet)"] *= 1.2
    elif anomaly_type == "temperature_drop":
        datapoint["Temperature (inlet)"] *= 0.8
        datapoint["Temperature (outlet)"] *= 0.9
    elif anomaly_type == "flow_decrease":
        datapoint["Flow Rate"] *= 0.7
    elif anomaly_type == "gas_concentration_surge":
        datapoint["Gas Concentration (ppm)"] *= 2.0
    datapoint["Anomalies Flag"] = "Yes"  # Set anomaly flag
    return datapoint

# Function to generate random alerts with codes
def generate_alert(datapoint):
    if random.random() < 0.01:  # 1% chance of an alert
        datapoint["Alert (on/off)"] = "on"
        alert_codes = ["P01", "T02", "F03", "G04"]  # Example alert codes
        datapoint["Alert Code"] = random.choice(alert_codes)
    return datapoint

# Function to introduce missing values and outliers
def introduce_imperfection(datapoint):
    if random.random() < 0.07:  # 5% chance of missing value
        missing_features = random.sample(list(features.keys()), 1)  # Pick one random feature
        for feature in missing_features:
            datapoint[feature] = None
    if random.random() < 0.03:  # 2% chance of outlier
        outlier_features = random.sample(list(features.keys()), 1)  # Pick one random feature
        for feature in outlier_features:
            if features[feature] == float:
                datapoint[feature] = base_value + random.uniform(-variation * 3, variation * 3)  # Extreme outlier
            else:
                datapoint[feature] = "NA"  # Outlier for non-numeric features
    return datapoint

# Open CSV file for writing
with open("oil_gas_sensor_data_imperfect.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=features.keys())
    writer.writeheader()

    # Generate timestamps for each data point
    from datetime import datetime, timedelta
    current_time = datetime.strptime(start_date, "%Y-%m-%d %H:%M:%S")
    end_time = datetime.strptime(end_date, "%Y-%m-%d %H:%M:%S")

    while current_time <= end_time:
        datapoint = {}

        # Generate sensor readings
        for feature, dtype in features.items():
            if feature == "Timestamp":
                datapoint[feature] = current_time.strftime("%Y-%m-%d %H:%M:%S")
            elif feature in ("Alert (on/off)", "Anomalies Flag"):
                datapoint[feature] = "off"
            else:
                base_value = random.randint(30, 100) if feature.startswith("Pressure") else random.randint(10, 50)
                variation = base_value * 0.1  # 10% variation
                datapoint[feature] = generate_sensor_reading(base_value, variation)

        # Introduce anomalies with a 2% chance
        datapoint = generate_anomaly(datapoint)

        # Introduce random alerts with codes
        datapoint = generate_alert(datapoint)

        # Introduce missing values and outliers
        datapoint = introduce_imperfection(datapoint)

        # Write data point to CSV
        writer.writerow(datapoint)

        # Increment time for next data point
        current_time += timedelta(minutes=frequency)

print("CSV file 'oil_gas_sensor_data_imperfect.csv' generated successfully!")