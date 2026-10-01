import pandas as pd
import joblib
from pathlib import Path


print("\n================================")
print("       SMART HELMET AI")
print("================================")


# ---------------------------------------------
# 1. Project paths
# ---------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = BASE_DIR / "ml" / "models" / "smart_helmet_model.pkl"
SCALER_PATH = BASE_DIR / "ml" / "models" / "smart_helmet_scaler.pkl"


# ---------------------------------------------
# 2. Load model and scaler
# ---------------------------------------------

model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

print("\nML model loaded successfully.")
print("Scaler loaded successfully.")


# ---------------------------------------------
# 3. Select condition
# ---------------------------------------------

print("\nSelect test condition:")
print("1. Normal condition")
print("2. Accident condition")

choice = input("\nEnter your choice (1 or 2): ")


# ---------------------------------------------
# 4. Use real dataset sensor values
# ---------------------------------------------

if choice == "1":

    # Real Normal sample from raw dataset

    sensor_values = {
        "accel_x": -0.562321,
        "accel_y": 0.109575,
        "accel_z": 10.078115,
        "gyro_x": 11.156501,
        "gyro_y": 7.689660,
        "gyro_z": 1.792268
    }

    expected_condition = "NORMAL"


elif choice == "2":

    # Real Accident sample from raw dataset

    sensor_values = {
        "accel_x": -1.389484,
        "accel_y": -7.479812,
        "accel_z": 7.728952,
        "gyro_x": 85.946640,
        "gyro_y": -58.809344,
        "gyro_z": -52.923315
    }

    expected_condition = "ACCIDENT"


else:

    print("\nInvalid choice.")
    exit()


# ---------------------------------------------
# 5. Display sensor values
# ---------------------------------------------

print("\n================================")
print("       SENSOR VALUES")
print("================================")

for name, value in sensor_values.items():
    print(f"{name}: {value}")


# ---------------------------------------------
# 6. Convert to DataFrame
# ---------------------------------------------

features = [
    "accel_x",
    "accel_y",
    "accel_z",
    "gyro_x",
    "gyro_y",
    "gyro_z"
]

sensor_df = pd.DataFrame(
    [sensor_values],
    columns=features
)


# ---------------------------------------------
# 7. Apply scaler
# ---------------------------------------------

scaled_sensor = scaler.transform(sensor_df)

scaled_sensor_df = pd.DataFrame(
    scaled_sensor,
    columns=features
)


# ---------------------------------------------
# 8. Predict
# ---------------------------------------------

prediction = model.predict(scaled_sensor_df)[0]


# ---------------------------------------------
# 9. Display prediction
# ---------------------------------------------

print("\n================================")
print("        ML PREDICTION")
print("================================")

print("Predicted label:", prediction)


if prediction == 0:

    print("Condition: NORMAL")
    print("Green LED: ON")
    print("Red LED: OFF")
    print("Buzzer: OFF")

    print("\nRider is safe.")
    print("No emergency alert required.")


elif prediction == 1:

    print("Condition: ACCIDENT")
    print("Green LED: OFF")
    print("Red LED: ON")
    print("Buzzer: ON")

    print("\nAccident detected!")
    print("Emergency alert system can be activated.")


print("\n================================")
print("Expected condition:", expected_condition)
print("================================")