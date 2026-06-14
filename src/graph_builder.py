import pandas as pd
import networkx as nx
import pickle

# Load processed delivery data
df = pd.read_csv("data/processed/processed_delivery2_data.csv")

# Create graph
G = nx.Graph()

# Add edges
for _, row in df.iterrows():
    G.add_edge(
        row["source"],
        row["destination"],
        distance_km=row["distance_km"]
    )

# Display graph information
print("\nGraph Statistics")
print("----------------")
print("Nodes:", G.number_of_nodes())
print("Edges:", G.number_of_edges())

# Display all edges with distances
print("\nEdges and Distances:")
for u, v, data in G.edges(data=True):
    print(f"{u} -> {v} : {data}")

# Save graph
with open("models/delivery_graph.pkl", "wb") as f:
    pickle.dump(G, f)

print("\nGraph saved successfully.")