import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath)
    return df

def preprocess_data(df):
    df = df.copy()

    weather_map = {
        "Clear": 0,
        "Cloudy": 1,
        "Rain": 2
    }

    df["weather_encoded"] = df["weather"].map(weather_map)

    return df

if __name__ == "__main__":
    df = load_data("data/raw/delivery2_data.csv")

    processed_df = preprocess_data(df)

    processed_df.to_csv(
        "data/processed/processed_delivery2_data.csv",
        index=False
    )

    print("Data preprocessing completed.")