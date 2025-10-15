# Repro script for transport clustering demo (SDG 11)
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
stops = pd.read_csv('stops_dataset.csv')
stops['log_passengers'] = (stops['daily_passengers']+1).apply(lambda x: __import__('math').log(x))
X = StandardScaler().fit_transform(stops[['x_coord','y_coord','log_passengers']])
km = KMeans(n_clusters=4, random_state=42, n_init=10).fit(X)
stops['cluster'] = km.labels_
stops.to_csv('stops_with_clusters.csv', index=False)
print('Saved stops_with_clusters.csv')