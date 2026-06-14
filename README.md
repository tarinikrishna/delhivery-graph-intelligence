# Delhivery Graph Intelligence

## Overview

This project uses Graph Analytics and Machine Learning to optimize logistics operations.

The solution models delivery centers as graph nodes and delivery routes as graph edges. Graph features are combined with operational metrics to improve ETA prediction and route recommendation.

## Features

### ETA Prediction

* Random Forest Regressor
* Predicts delivery time using:

  * Distance
  * OSRM Time
  * Graph Features

### Route Recommendation

* NetworkX Shortest Path Algorithm
* Recommends optimal routes between centers

### Graph Intelligence

* Degree Centrality
* Betweenness Centrality
* PageRank

### Dashboard

* Streamlit Interface
* ETA Prediction
* Route Recommendation
* Network Statistics

---

## Technology Stack

* Python
* Pandas
* NetworkX
* Scikit-Learn
* Streamlit
* Joblib

---

## Project Structure

data/
models/
notebooks/
src/
dashboard/

---

## Results

* Nodes: 1657
* Edges: 2783

---

## Future Improvements

* Dynamic Graph Feature Extraction
* Real-Time ETA Prediction
* Route Visualization
* Traffic-Aware Routing

---
## live demo:
https://delhivery-graph-intelligence-mayvyclrhbtu4oqoqyjzjj.streamlit.app/ 
## Author

tarinikrishna
