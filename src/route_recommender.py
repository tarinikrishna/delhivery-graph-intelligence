import pickle
import networkx as nx

# Load graph
with open("models/delivery_graph.pkl", "rb") as f:
    G = pickle.load(f)

# Source and destination
source = "WH_A"
destination = "CUST_5"

try:
    # Find shortest route based on distance
    shortest_path = nx.shortest_path(
        G,
        source=source,
        target=destination,
        weight="distance_km"
    )

    # Calculate total distance
    total_distance = nx.shortest_path_length(
        G,
        source=source,
        target=destination,
        weight="distance_km"
    )

    print("\nOptimal Route:")
    print(" -> ".join(shortest_path))

    print(f"\nTotal Distance: {total_distance} km")

except nx.NetworkXNoPath:
    print("No route exists between the selected nodes.")

except Exception as e:
    print(f"Error: {e}")