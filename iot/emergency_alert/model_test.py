import os
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


MODEL_PATH = os.path.join(
    "ml",
    "models",
    "smart_helmet_model.pkl"
)

TEST_PATH = os.path.join(
    "ml",
    "dataset",
    "processed",
    "test_data.csv"
)


FEATURES = [
    "accel_x",
    "accel_y",
    "accel_z",
    "gyro_x",
    "gyro_y",
    "gyro_z"
]


print("\n================================")
print("     SMART HELMET MODEL TEST")
print("================================")


# Load model
model = joblib.load(MODEL_PATH)

print("\nML model loaded successfully.")


# Load test data
test_data = pd.read_csv(TEST_PATH)

print("\nTest data loaded.")
print("Rows:", len(test_data))


# Separate features and labels
X_test = test_data[FEATURES]
y_test = test_data["label"]


# Predictions
y_pred = model.predict(X_test)


# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\n================================")
print("          RESULTS")
print("================================")

print("Accuracy:", accuracy)


# Confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# Classification report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


print("\n================================")