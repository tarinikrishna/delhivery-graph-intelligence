import pandas as pd
import networkx as nx

def add_graph_features(df, G):

    degree = nx.degree_centrality(G)

    pagerank = nx.pagerank(G)

    betweenness = nx.betweenness_centrality(
        G,
        k=100,
        seed=42
    )

    df["source_degree"] = (
        df["source_center"]
        .map(degree)
        .fillna(0)
    )

    df["destination_degree"] = (
        df["destination_center"]
        .map(degree)
        .fillna(0)
    )

    df["source_pagerank"] = (
        df["source_center"]
        .map(pagerank)
        .fillna(0)
    )

    df["destination_pagerank"] = (
        df["destination_center"]
        .map(pagerank)
        .fillna(0)
    )

    return df