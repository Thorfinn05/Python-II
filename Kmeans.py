# Required Libraries
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
# Load the Iris dataset
iris = load_iris()
data = iris.data
print(data)
target = iris.target
print(iris.target)
# Perform K-means clustering and take cluster centers
kmeans_model = KMeans(n_clusters=3, random_state=1).fit(data)
labels = kmeans_model.labels_
clusters_sklearn = kmeans_model.cluster_centers_
print(labels)
print(kmeans_model.cluster_centers_)
# Function to plot final clusters
def plot_clusters_sklearn(data, labels, clusters):
    # Plot data points, choosing first two features for visualization
    plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', label='Data points')
    # Plot cluster centers, also focusing on the same two features
    plt.scatter(clusters[:, 0], clusters[:, 1], s=200, color='red', marker='X', label='Centers')
    plt.title('Visualizing Clusters with Matplotlib using Iris Dataset')
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Sepal Width (cm)')
    plt.legend()
    plt.grid(True)
    plt.show()
# Visualize the clusters
plot_clusters_sklearn(data, labels, clusters_sklearn)