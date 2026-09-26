import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Project paths
BASE_DIR = Path(__file__).resolve().parents[2]

DATA_PATH = BASE_DIR / "ml" / "dataset" / "processed" / "smart_helmet_processed.csv"
OUTPUT_DIR = BASE_DIR / "ml" / "dataset" / "processed"

# --------------------------------------------------
# 1. Load dataset
# --------------------------------------------------

df = pd.read_csv(DATA_PATH)

print("Dataset loaded successfully!")
print("Original shape:", df.shape)

# --------------------------------------------------
# 2. Check duplicate rows
# --------------------------------------------------

duplicates = df.duplicated().sum()
print("Duplicate rows:", duplicates)

if duplicates > 0:
    df = df.drop_duplicates()
    print("Duplicates removed.")
else:
    print("No duplicate rows found.")

# --------------------------------------------------
# 3. Separate features and label
# --------------------------------------------------

features = [
    "accel_x",
    "accel_y",
    "accel_z",
    "gyro_x",
    "gyro_y",
    "gyro_z"
]

X = df[features]
y = df["label"]

print("\nFeatures:")
print(features)

print("\nFeature shape:", X.shape)
print("Label shape:", y.shape)

# --------------------------------------------------
# 4. Split into training and testing data
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# --------------------------------------------------
# 5. Scale sensor features
# --------------------------------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

print("\nFeature scaling completed.")

# --------------------------------------------------
# 6. Convert scaled data back to DataFrames
# --------------------------------------------------

X_train_scaled = pd.DataFrame(
    X_train_scaled,
    columns=features
)

X_test_scaled = pd.DataFrame(
    X_test_scaled,
    columns=features
)

# Add labels
X_train_scaled["label"] = y_train.reset_index(drop=True)
X_test_scaled["label"] = y_test.reset_index(drop=True)

# --------------------------------------------------
# 7. Save processed datasets
# --------------------------------------------------

train_path = OUTPUT_DIR / "train_data.csv"
test_path = OUTPUT_DIR / "test_data.csv"

X_train_scaled.to_csv(train_path, index=False)
X_test_scaled.to_csv(test_path, index=False)

print("\nProcessed datasets saved successfully!")

print("Training data:", train_path)
print("Testing data:", test_path)

print("\nPreprocessing completed successfully!")