import joblib
import pandas as pd
import time
import threading
from pathlib import Path
from emergency_message import send_emergency_message

# ==================================================
# 1. PROJECT PATHS
# ==================================================

BASE_DIR = Path(__file__).resolve().parents[2]

MODEL_PATH = BASE_DIR / "ml" / "models" / "smart_helmet_model.pkl"
SCALER_PATH = BASE_DIR / "ml" / "models" / "smart_helmet_scaler.pkl"


# ==================================================
# 2. LOAD ML MODEL AND SCALER
# ==================================================

print("================================")
print("       SMART HELMET AI")
print("================================")

try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)

    print("\nML model loaded successfully.")
    print("Scaler loaded successfully.")

except Exception as e:
    print("\nError loading model or scaler:")
    print(e)
    exit()


# ==================================================
# 3. SELECT TEST CONDITION
# ==================================================

print("\nSelect test condition:")
print("1. Normal condition")
print("2. Accident condition")

choice = input("\nEnter your choice (1 or 2): ").strip()


# ==================================================
# 4. TEST SENSOR VALUES
# ==================================================

if choice == "1":

    # Normal sensor values
    sensor_data = {
        "accel_x": -0.562321,
        "accel_y": 0.109575,
        "accel_z": 10.078115,
        "gyro_x": 11.156501,
        "gyro_y": 7.689660,
        "gyro_z": 1.792268
    }

    expected_condition = "NORMAL"


elif choice == "2":

    # Accident sensor values
    sensor_data = {
        "accel_x": -1.389484,
        "accel_y": -7.479812,
        "accel_z": 7.728952,
        "gyro_x": 85.946640,
        "gyro_y": -58.809344,
        "gyro_z": -52.923315
    }

    expected_condition = "ACCIDENT"


else:

    print("\nInvalid choice!")
    print("Please enter either 1 or 2.")
    exit()


# ==================================================
# 5. DISPLAY SENSOR VALUES
# ==================================================

print("\n================================")
print("       SENSOR VALUES")
print("================================")

for name, value in sensor_data.items():
    print(f"{name}: {value}")


# ==================================================
# 6. PREPARE DATA FOR ML MODEL
# ==================================================

features = [
    "accel_x",
    "accel_y",
    "accel_z",
    "gyro_x",
    "gyro_y",
    "gyro_z"
]

sensor_df = pd.DataFrame([sensor_data], columns=features)


# ==================================================
# 7. SCALE SENSOR DATA
# ==================================================

sensor_scaled = scaler.transform(sensor_df)

sensor_scaled_df = pd.DataFrame(
    sensor_scaled,
    columns=features
)


# ==================================================
# 8. ML PREDICTION
# ==================================================

prediction = model.predict(sensor_scaled_df)[0]


# ==================================================
# 9. DISPLAY ML RESULT
# ==================================================

print("\n================================")
print("        ML PREDICTION")
print("================================")

print("Predicted label:", prediction)


# ==================================================
# 10. NORMAL CONDITION
# ==================================================

if prediction == 0:

    print("Condition: NORMAL")

    print("Green LED: ON")
    print("Red LED: OFF")
    print("Buzzer: OFF")

    print("\nRider is safe.")
    print("No emergency alert required.")


# ==================================================
# 11. ACCIDENT CONDITION
# ==================================================

elif prediction == 1:

    print("Condition: ACCIDENT")

    print("Green LED: OFF")
    print("Red LED: ON")
    print("Buzzer: ON")

    print("\nWARNING! ACCIDENT DETECTED!")

    print("\nYou have 15 seconds to confirm that you are safe.")
    print("Type YES and press Enter to cancel the emergency alert.")


    # --------------------------------------------------
    # Safety confirmation
    # --------------------------------------------------

    user_input = [None]


    def get_confirmation():
        user_input[0] = input("\nType YES if you are safe: ")


    input_thread = threading.Thread(
        target=get_confirmation
    )

    input_thread.daemon = True
    input_thread.start()


    # --------------------------------------------------
    # 15 SECOND TIMER
    # --------------------------------------------------

    for remaining in range(15, 0, -1):

        if user_input[0] is not None:
            break

        print(f"Time remaining: {remaining} seconds")
        time.sleep(1)


    # ==================================================
    # 12. RIDER CONFIRMED SAFE
    # ==================================================

    if (
        user_input[0] is not None
        and user_input[0].strip().upper() == "YES"
    ):

        print("\nSafety confirmation received.")
        print("Emergency alert cancelled.")


    # ==================================================
    # 13. NO CONFIRMATION
    # ==================================================

    else:

        print("\nNo safety confirmation received.")
        print("Emergency alert triggered!")

        print("\n================================")
        print("       EMERGENCY ALERT")
        print("================================")

        print("Red LED: ON")
        print("Buzzer: ON")

        # --------------------------------------------------
        # GPS SIMULATION
        # --------------------------------------------------

        latitude = 17.6868
        longitude = 83.2185

        print("\nGPS Location:")
        print("Latitude:", latitude)
        print("Longitude:", longitude)

        maps_link = (
            f"https://www.google.com/maps?"
            f"q={latitude},{longitude}"
        )

        print("\nLocation:")
        print(maps_link)

        # --------------------------------------------------
        # Emergency Message
        # --------------------------------------------------

        send_emergency_message(latitude, longitude)


# ==================================================
# 14. EXPECTED CONDITION
# ==================================================

print("\n================================")
print("Expected condition:", expected_condition)
print("================================")

print("\nSystem execution completed.")