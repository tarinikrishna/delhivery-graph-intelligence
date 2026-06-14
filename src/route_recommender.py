import networkx as nx

def recommend_route(
    G,
    source,
    destination
):

    try:

        path = nx.shortest_path(
            G,
            source,
            destination,
            weight="weight"
        )

        return path

    except:

        return None