import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Creating the DataFrame
data = {
    'Maths': [88, 74, 75, 62, 81, 90, 70, 69, 65, 93],
    'Science': [75, 80, 85, 78, 92, 96, 82, 70, 74, 88],
    'English': [92, 78, 79, 73, 85, 87, 78, 65, 72, 91],
    'History': [67, 72, 78, 65, 83, 76, 74, 60, 64, 85],
    'Computer Science': [85, 90, 85, 77, 91, 89, 81, 64, 76, 95]
}

df = pd.DataFrame(data)

# Elbow Method to find optimal K
inertia = []

for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=1, n_init=10)
    kmeans.fit(df)
    inertia.append(kmeans.inertia_)

# Plotting the Elbow Curve
plt.figure(figsize=(8,5))
plt.plot(range(1, 11), inertia, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia')
plt.grid(True)
plt.show()

# Perform K-means clustering and take cluster centers
kmeans_model = KMeans(n_clusters=3, random_state=1, n_init=10).fit(df)
labels = kmeans_model.labels_
clusters_sklearn = kmeans_model.cluster_centers_
print(labels)
print(kmeans_model.cluster_centers_)

# Function to plot final clusters (choosing two features only, e.g., Maths and Science)
def plot_clusters_sklearn(data, labels, clusters):
    # Plot data points
    plt.scatter(data[:, 0], data[:, 1], c=labels, cmap='viridis', label='Data points')
    # Plot cluster centers
    plt.scatter(clusters[:, 0], clusters[:, 1], s=200, color='red', marker='X', label='Centers')
    plt.title('Visualizing Clusters with Maths and Science Scores')
    plt.xlabel('Maths Score')
    plt.ylabel('Science Score')
    plt.legend()
    plt.grid(True)
    plt.show()

# Select only 'Maths' and 'Science' columns for plotting
selected_features = df[['Maths', 'Science']].values

# Fit again using only selected features
kmeans_selected = KMeans(n_clusters=3, random_state=1, n_init=10).fit(selected_features)
labels_selected = kmeans_selected.labels_
clusters_selected = kmeans_selected.cluster_centers_

# Visualize the clusters
plot_clusters_sklearn(selected_features, labels_selected, clusters_selected)
