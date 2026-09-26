import pandas as pd
from pathlib import Path

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib


# --------------------------------------------------
# 1. Project paths
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parents[2]

TRAIN_PATH = BASE_DIR / "ml" / "dataset" / "processed" / "train_data.csv"
TEST_PATH = BASE_DIR / "ml" / "dataset" / "processed" / "test_data.csv"

MODEL_DIR = BASE_DIR / "ml" / "models"
MODEL_DIR.mkdir(parents=True, exist_ok=True)

MODEL_PATH = MODEL_DIR / "smart_helmet_model.pkl"


# --------------------------------------------------
# 2. Load training and testing data
# --------------------------------------------------

train_data = pd.read_csv(TRAIN_PATH)
test_data = pd.read_csv(TEST_PATH)

print("Training data loaded:", train_data.shape)
print("Testing data loaded:", test_data.shape)


# --------------------------------------------------
# 3. Separate features and labels
# --------------------------------------------------

features = [
    "accel_x",
    "accel_y",
    "accel_z",
    "gyro_x",
    "gyro_y",
    "gyro_z"
]

X_train = train_data[features]
y_train = train_data["label"]

X_test = test_data[features]
y_test = test_data["label"]


# --------------------------------------------------
# 4. Create the ML model
# --------------------------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# --------------------------------------------------
# 5. Train the model
# --------------------------------------------------

print("\nTraining the ML model...")

model.fit(X_train, y_train)

print("Training completed!")


# --------------------------------------------------
# 6. Test the model
# --------------------------------------------------

y_pred = model.predict(X_test)


# --------------------------------------------------
# 7. Calculate accuracy
# --------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)


# --------------------------------------------------
# 8. Classification report
# --------------------------------------------------

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# --------------------------------------------------
# 9. Confusion matrix
# --------------------------------------------------

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# --------------------------------------------------
# 10. Save the trained model
# --------------------------------------------------

joblib.dump(model, MODEL_PATH)

print("\nModel saved successfully!")
print("Model path:", MODEL_PATH)