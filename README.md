# AI for Sustainable Development – SDG 11 Project
Machine Learning Meets the UN Sustainable Development Goals (SDGs)

Focus: SDG 11 – Sustainable Cities and Communities
Project Title: Optimizing Urban Transport Routes Using K-Means Clustering

# OVERVIEW:

This project demonstrates how machine learning can support the United Nations’ Sustainable Development Goal 11 (Make cities inclusive, safe, resilient, and sustainable) by improving urban transportation efficiency.
Using unsupervised learning (K-Means Clustering), the model identifies optimal transit hub locations based on spatial and passenger demand data. This AI-driven insight helps urban planners design more efficient, accessible, and sustainable transport networks

# Objectives

- Analyze urban bus stop and ridership data.
- Group similar transit stops using clustering.
- Identify optimal central hubs to reduce travel time and congestion.
- Demonstrate how AI can promote sustainability and fairness in urban planning.

# Machine Learning Approach

# Algorithm: K-Means Clustering

# Learning Type: Unsupervised Learning

# Model Selection: Optimal k determined via Silhouette Score

# Tools & Libraries:
- Python
- Scikit-learn
- Pandas
- Matplotlib
- Jupyter Notebook

# Dataset

A synthetic dataset of 300 urban bus stops was created, including:
- Stop coordinates (X, Y)
- Daily passenger demand
- The dataset simulates real-world ridership patterns and urban density variations

# Results Summary

- Best cluster count: k = 4
- Outcome: Four distinct service zones and their central hub locations identified.
- Evaluation:
Silhouette Score → For cluster quality
Inertia → For compactness

# Visualizations:
- Elbow curve
- Silhouette score plot
- Cluster map with hub markers

# Ethical and Sustainability Considerations

- Data Bias: Ensure representation of all socioeconomic areas.
- Privacy: Anonymize GPS and ridership data before analysis.
- Fairness: Optimize service distribution equitably across demographics.
- Sustainability Impact: Reduced emissions through efficient routing and fewer redundant trip

# PROJECT STRUCTURE

transport_clustering_demo/
│
├── stops_dataset.csv              # Simulated dataset of bus stops
├── cluster_summary.csv            # Cluster results and centroids
├── repro_demo.py                  # Python script for reproducibility
├── transport_clustering_demo.ipynb# Jupyter Notebook with workflow
├── elbow_inertia.png              # Elbow method visualization
├── silhouette_scores.png          # Silhouette analysis plot
├── clusters_and_hubs.png          # Final cluster visualization
├── AI_for_SDG11_Report.pdf        # 1-page summary report
└── AI_for_SDG11_Presentation.pptx # 5-slide presentation

# How to Run

Extract the ZIP file:

- unzip transport_clustering_demo.zip
- cd transport_clustering_demo

Open the Jupyter notebook:

- jupyter notebook transport_clustering_demo.ipynb

Run all cells to reproduce the analysis and visualizations

# Future Improvements

- Integrate real-world transit datasets (e.g., GTFS data).
- Include travel time, emission data, and socioeconomic indicators.
- Deploy as a web-based visualization dashboard for planners.

# Author

Kenneth Ifeanyi Ukorah 
ukorahkenneth@gmail.com
AI for Sustainable Development – Week 2 Project
