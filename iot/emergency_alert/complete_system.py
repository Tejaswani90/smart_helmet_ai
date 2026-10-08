import joblib
import pandas as pd
from pathlib import Path

# Import GPS function
from gps import get_gps_location

# Import safety confirmation
from safety_button import wait_for_safety_confirmation

# Import emergency message
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

    print("\nERROR: Could not load ML model or scaler.")
    print("Reason:", e)

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
    print("Please enter 1 or 2.")

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

sensor_df = pd.DataFrame(
    [sensor_data],
    columns=features
)


# ==================================================
# 7. SCALE SENSOR DATA
# ==================================================

try:

    sensor_scaled = scaler.transform(sensor_df)

    # Convert scaled data back to DataFrame
    # so that feature names are preserved
    sensor_scaled_df = pd.DataFrame(
        sensor_scaled,
        columns=features
    )

except Exception as e:

    print("\nERROR during data scaling:")
    print(e)

    exit()


# ==================================================
# 8. ML PREDICTION
# ==================================================

try:

    prediction = model.predict(sensor_scaled_df)[0]

except Exception as e:

    print("\nERROR during ML prediction:")
    print(e)

    exit()


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

    print("\nCondition: NORMAL")

    print("Green LED: ON")
    print("Red LED: OFF")
    print("Buzzer: OFF")

    print("\nRider is safe.")
    print("No emergency alert required.")


# ==================================================
# 11. ACCIDENT CONDITION
# ==================================================

elif prediction == 1:

    print("\nCondition: ACCIDENT")

    print("Green LED: OFF")
    print("Red LED: ON")
    print("Buzzer: ON")

    print("\nWARNING! ACCIDENT DETECTED!")


    # ==================================================
    # SAFETY CONFIRMATION
    # ==================================================

    safety_confirmed = wait_for_safety_confirmation(
        timeout=15
    )


    # ==================================================
    # RIDER CONFIRMED SAFE
    # ==================================================

    if safety_confirmed:

        print("\n================================")
        print("       SAFETY CONFIRMED")
        print("================================")

        print("Rider confirmed that they are safe.")
        print("Emergency alert cancelled.")


    # ==================================================
    # NO SAFETY CONFIRMATION
    # ==================================================

    else:

        print("\n================================")
        print("       EMERGENCY ALERT")
        print("================================")

        print("No safety confirmation received.")
        print("Emergency alert triggered!")

        print("\nRed LED: ON")
        print("Buzzer: ON")


        # ==================================================
        # GET GPS LOCATION
        # ==================================================

        print("\nGetting GPS location...")

        try:

            latitude, longitude, maps_link = get_gps_location()

            print("\nGPS Location:")
            print("Latitude :", latitude)
            print("Longitude:", longitude)

            print("\nGoogle Maps Location:")
            print(maps_link)

        except Exception as e:

            print("\nERROR while getting GPS location:")
            print(e)

            latitude = None
            longitude = None
            maps_link = None


        # ==================================================
        # SEND EMERGENCY MESSAGE
        # ==================================================

        if latitude is not None and longitude is not None:

            try:

                send_emergency_message(
                    latitude,
                    longitude
                )

                print("\nEmergency message sent successfully.")

            except Exception as e:

                print("\nERROR while sending emergency message:")
                print(e)

        else:

            print(
                "\nEmergency message could not include GPS location."
            )


# ==================================================
# 12. UNEXPECTED PREDICTION
# ==================================================

else:

    print(
        "\nUnexpected ML prediction:",
        prediction
    )


# ==================================================
# 13. FINAL STATUS
# ==================================================

print("\n================================")
print(
    "Expected condition:",
    expected_condition
)
print("================================")

print("\nSystem execution completed.")