import pandas as pd
import joblib

# --------------------------------------------------
# 1. Load the trained model and scaler
# --------------------------------------------------

model_path = "ml/models/smart_helmet_model.pkl"
scaler_path = "ml/models/scaler.pkl"

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

# --------------------------------------------------
# 2. New sensor reading
# --------------------------------------------------

new_data = pd.DataFrame([{
    "accel_x": -1.354577,
    "accel_y": 0.533559,
    "accel_z": 0.941766,
    "gyro_x": -1.737625,
    "gyro_y": 1.056825,
    "gyro_z": -1.338347
}])

# --------------------------------------------------
# 3. Scale the new sensor data
# --------------------------------------------------

scaled_data = scaler.transform(new_data)

scaled_data = pd.DataFrame(
    scaled_data,
    columns=new_data.columns
)

# --------------------------------------------------
# 4. Make prediction
# --------------------------------------------------

prediction = model.predict(scaled_data)[0]

# --------------------------------------------------
# 5. Display result
# --------------------------------------------------

print("New sensor data:")
print(new_data)

print("\nPrediction:", prediction)

if prediction == 1:
    print("Result: Accident condition detected")
elif prediction == 0:
    print("Result: Helmet normal")
else:
    print("Result: Unknown condition")