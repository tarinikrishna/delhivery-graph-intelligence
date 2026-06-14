import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import pickle

# Load delivery data
df = pd.read_csv("data/raw/delivery2_data.csv")

# Encode weather column
weather_map = {
    "Clear": 0,
    "Cloudy": 1,
    "Rain": 2
}

df["weather_encoded"] = df["weather"].map(weather_map)

# Features
X = df[
    [
        "distance_km",
        "traffic_level",
        "weather_encoded"
    ]
]

# Target variable
y = df["delivery_time"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create Random Forest model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)

# Evaluate model
mae = mean_absolute_error(y_test, predictions)

print(f"Mean Absolute Error: {mae:.2f} minutes")

# Save trained model
with open("models/random_forest_eta.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model saved successfully.")