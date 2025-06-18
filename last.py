import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

dataset = load_iris()
data = pd.DataFrame(dataset.data, columns=dataset.feature_names)
data['species'] = pd.Categorical.from_codes(dataset.target, dataset.target_names)

print(dataset.feature_names)
print(dataset.target_names)

def plot_clusters_sklearn(data, labels, clusters):
    plt.scatter(data[:,0], data[:,1], c=labels, cmap='viridis', label='Data points')
    plt.scatter(clusters[:,0], clusters[:,1], s=200, marker='X', color = 'red', label='Clusters')
    plt.legend()
    plt.grid(True)
    plt.show()

features=data.drop('species', axis=1)

kmeans_selected = KMeans(n_clusters=3, random_state=1, n_init=10).fit(features)
labels_selected = kmeans_selected.labels_
clusters_selected = kmeans_selected.cluster_centers_

plot_clusters_sklearn(features.values, labels_selected, clusters_selected)

sse = []
k_range = range(1,11)
for k in k_range:
    kmeans=KMeans(n_clusters=k, random_state=1, n_init=10).fit(features)
    sse.append(kmeans.inertia_)

plt.plot(k_range, sse)
plt.xticks(k_range)
plt.show()

iris_setosa = data.loc[data['species']=='setosa']
counts, bin_edges = np.histogram(iris_setosa['petal length (cm)'], bins=10, density=True)
pdf = counts/sum(counts)
print(pdf)
print(bin_edges)
cdf=np.cumsum(pdf)
print(cdf)

plt.plot(bin_edges[1:], pdf, label='pdf')
plt.plot(bin_edges[1:], cdf, label='cdf')
plt.grid()
plt.legend()
plt.show()