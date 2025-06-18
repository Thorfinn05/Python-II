import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

# Load and prepare data
dataset = load_iris()
data = pd.DataFrame(dataset.data, columns=dataset.feature_names)
data['species'] = pd.Categorical.from_codes(dataset.target, dataset.target_names)

print("Feature names:", dataset.feature_names)
print("Target names:", dataset.target_names)

# Function to plot clusters (on first 2 features)
def plot_clusters_sklearn(data, labels, clusters):
    plt.figure(figsize=(8,6))
    plt.scatter(data[:,0], data[:,1], c=labels, cmap='viridis', label='Data points')
    plt.scatter(clusters[:,0], clusters[:,1], s=200, marker='X', color='red', label='Clusters')
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.legend()
    plt.grid(True)
    plt.title("KMeans Clustering (2D Projection)")
    plt.show()

# Select features (remove species)
features = data.drop('species', axis=1)

# Apply KMeans with k=3
kmeans_selected = KMeans(n_clusters=3, random_state=1, n_init=10).fit(features)
labels_selected = kmeans_selected.labels_
clusters_selected = kmeans_selected.cluster_centers_

# Visualize clusters (only first 2 features)
plot_clusters_sklearn(features.values[:, :2], labels_selected, clusters_selected[:, :2])

# Elbow method to find optimal k
sse = []
k_range = range(1, 11)
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=1, n_init=10).fit(features)
    sse.append(kmeans.inertia_)

plt.figure(figsize=(8,5))
plt.plot(k_range, sse, marker='o')
plt.xticks(k_range)
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Sum of Squared Errors (SSE)")
plt.title("Elbow Method for Optimal k")
plt.grid()
plt.show()

# PDF and CDF for Iris-setosa petal length
iris_setosa = data.loc[data['species'] == 'setosa']
counts, bin_edges = np.histogram(iris_setosa['petal length (cm)'], bins=10, density=True)
pdf = counts / sum(counts)
cdf = np.cumsum(pdf)

print("PDF:", pdf)
print("Bin Edges:", bin_edges)
print("CDF:", cdf)

plt.figure(figsize=(8,5))
plt.plot(bin_edges[1:], pdf, label='PDF', marker='o')
plt.plot(bin_edges[1:], cdf, label='CDF', marker='x')
plt.xlabel("Petal Length (cm)")
plt.title("PDF and CDF of Petal Length for Iris-Setosa")
plt.grid()
plt.legend()
plt.show()
