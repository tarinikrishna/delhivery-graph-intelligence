import sys
import os
import joblib
import streamlit as st

sys.path.append(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "src"
    )
)

from route_recommender import recommend_route

graph_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "delivery_graph.pkl"
)

G = joblib.load(graph_path)

model_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "models",
    "random_forest_eta.pkl"
)

model = joblib.load(model_path)

st.title("Delhivery Graph Intelligence")

# ETA Prediction

st.header("ETA Prediction")

distance = st.number_input(
    "Distance",
    min_value=0.0
)

osrm_time = st.number_input(
    "OSRM Time",
    min_value=0.0
)

if st.button("Predict ETA"):

    prediction = model.predict([
        [
            distance,
            osrm_time,
            distance,
            1,
            1,
            0.01,
            0.01,
            0.001,
            0.001
        ]
    ])

    st.success(
        f"Predicted ETA: {prediction[0]:.2f} minutes"
    )

# Route Recommendation

st.header("Route Recommendation")

source = st.text_input(
    "Source Center"
)

destination = st.text_input(
    "Destination Center"
)

if st.button("Find Route"):

    route = recommend_route(
        G,
        source,
        destination
    )

    if route:
        st.success("Route Found!")
        st.write(route)

    else:
        st.error("No route found")

# Network Statistics

st.header("Network Statistics")

st.write(
    "Number of Nodes:",
    G.number_of_nodes()
)

st.write(
    "Number of Edges:",
    G.number_of_edges()
)