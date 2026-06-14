import streamlit as st
import pandas as pd
import networkx as nx
import pickle
import matplotlib.pyplot as plt

# --------------------------------------------------
# Page Config
# --------------------------------------------------

st.set_page_config(
    page_title="Delhivery Graph Intelligence",
    page_icon="🚚",
    layout="wide"
)

# --------------------------------------------------
# Custom CSS
# --------------------------------------------------

st.markdown("""
<style>

.stApp{
    background-color:#0f172a;
}

h1,h2,h3,h4,h5,h6,p,label{
    color:white;
}

.hero{
    background:linear-gradient(90deg,#2563eb,#06b6d4);
    padding:25px;
    border-radius:20px;
    text-align:center;
    box-shadow:0px 10px 25px rgba(0,0,0,0.3);
    margin-bottom:25px;
}

.metric-card{
    background:rgba(255,255,255,0.08);
    backdrop-filter:blur(10px);
    padding:20px;
    border-radius:15px;
    text-align:center;
    border:1px solid rgba(255,255,255,0.1);
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Hero Section
# --------------------------------------------------

st.markdown("""
<div class='hero'>
<h1>🚚 Delhivery Graph Intelligence Dashboard</h1>
<h3>AI-Powered Route Optimization & ETA Prediction</h3>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Load Graph
# --------------------------------------------------

with open("models/delivery_graph.pkl", "rb") as f:
    G = pickle.load(f)

# --------------------------------------------------
# Load ETA Model
# --------------------------------------------------

with open("models/random_forest_eta.pkl", "rb") as f:
    model = pickle.load(f)

# --------------------------------------------------
# Inputs
# --------------------------------------------------

nodes = list(G.nodes())

col1, col2 = st.columns(2)

with col1:
    source = st.selectbox(
        "📍 Select Source",
        nodes
    )

with col2:
    destination = st.selectbox(
        "🎯 Select Destination",
        nodes
    )

col3, col4 = st.columns(2)

with col3:
    traffic = st.selectbox(
        "🚦 Traffic Condition",
        ["Low", "Medium", "High"]
    )

with col4:
    weather = st.selectbox(
        "🌦 Weather",
        ["Clear", "Cloudy", "Rain"]
    )

# --------------------------------------------------
# Button
# --------------------------------------------------

if st.button("🚚 Find Optimal Route"):

    try:

        shortest_path = nx.shortest_path(
            G,
            source=source,
            target=destination,
            weight="distance_km"
        )

        distance = nx.shortest_path_length(
            G,
            source=source,
            target=destination,
            weight="distance_km"
        )

        # ------------------------------------------
        # ETA Prediction
        # ------------------------------------------

        traffic_map = {
            "Low":1,
            "Medium":2,
            "High":3
        }

        weather_map = {
            "Clear":0,
            "Cloudy":1,
            "Rain":2
        }

        eta = model.predict(
            [[
                distance,
                traffic_map[traffic],
                weather_map[weather]
            ]]
        )[0]

        # ------------------------------------------
        # Success Message
        # ------------------------------------------

        st.success("✅ Optimal Route Found")

        # ------------------------------------------
        # KPI Cards
        # ------------------------------------------

        colA, colB, colC = st.columns(3)

        with colA:
            st.metric(
                "📍 Distance",
                f"{distance} km"
            )

        with colB:
            st.metric(
                "⏱ ETA",
                f"{eta:.2f} min"
            )

        with colC:
            st.metric(
                "🛣 Route Nodes",
                len(shortest_path)
            )

        st.markdown("---")

        # ------------------------------------------
        # Route
        # ------------------------------------------

        st.subheader("🛣 Optimal Route")

        route_text = " ➜ ".join(shortest_path)

        st.markdown(
            f"### {route_text}"
        )

        # ------------------------------------------
        # Analytics
        # ------------------------------------------

        st.subheader("📊 Route Analytics")

        analytics_df = pd.DataFrame({
            "Metric":[
                "Source",
                "Destination",
                "Distance (km)",
                "ETA (minutes)",
                "Traffic",
                "Weather"
            ],
            "Value":[
                source,
                destination,
                distance,
                round(eta,2),
                traffic,
                weather
            ]
        })

        st.dataframe(
            analytics_df,
            use_container_width=True
        )

        # ------------------------------------------
        # Network Graph
        # ------------------------------------------

        st.subheader("🌐 Logistics Network")

        fig, ax = plt.subplots(
            figsize=(12,8)
        )

        pos = nx.spring_layout(
            G,
            seed=42
        )

        nx.draw(
            G,
            pos,
            with_labels=True,
            node_size=3000,
            node_color="#60a5fa",
            font_size=11,
            font_weight="bold",
            edge_color="#06b6d4",
            width=2,
            ax=ax
        )

        edge_labels = nx.get_edge_attributes(
            G,
            "distance_km"
        )

        nx.draw_networkx_edge_labels(
            G,
            pos,
            edge_labels=edge_labels,
            ax=ax
        )

        plt.title(
            "Delivery Network Graph",
            fontsize=16
        )

        st.pyplot(fig)

    except nx.NetworkXNoPath:

        st.error(
            "❌ No route exists between selected nodes."
        )