import pickle
import pandas as pd
import networkx as nx

# Load graph
with open("models/delivery_graph.pkl", "rb") as f:
    G = pickle.load(f)

# Degree Centrality
degree_centrality = nx.degree_centrality(G)

# Betweenness Centrality
betweenness_centrality = nx.betweenness_centrality(G)

# Closeness Centrality
closeness_centrality = nx.closeness_centrality(G)

features = []

for node in G.nodes():

    features.append({
        "node": node,
        "degree_centrality": degree_centrality[node],
        "betweenness_centrality": betweenness_centrality[node],
        "closeness_centrality": closeness_centrality[node]
    })

feature_df = pd.DataFrame(features)

feature_df.to_csv(
    "data/processed/graph_features_v2.csv",
    index=False
)

print("Graph feature extraction completed.")
print(feature_df.head())