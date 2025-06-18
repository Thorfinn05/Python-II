import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

dataset = load_iris()
data = pd.DataFrame(dataset.data, columns=dataset.feature_names)
data['species'] = pd.Categorical.from_codes(dataset.target, dataset.target_names)

print(data)

print(data.head())
print(data.describe())
print(data.sample(10))
print(data.columns)
print(len(data.columns))
print(data.shape)
print(data.iloc[5:11])
print(data[['petal width (cm)', 'petal length (cm)']])
print(data[['sepal width (cm)']])
print(data['species'].value_counts())
print(data[data['species'] == 'setosa'])
print(data['petal length (cm)'].sum())
print(data['petal length (cm)'].mean())
print(data['petal length (cm)'].mode())
print(data['petal length (cm)'].max())
print(data['petal length (cm)'].min())
data.rename(columns={'sepal width (cm)':'sepal width', 'petal width (cm)':'petal width'}, inplace=True)
print(data.columns)
print(data.sample(5))
data.to_csv("new.csv")
plt.plot(data['species'])
plt.xlabel("No. of data points")
plt.show()
plt.hist(data['species'], color='green')
plt.show()
sb.set_style('whitegrid')
sb.scatterplot(data=data, x='sepal length (cm)', y='sepal width (cm)', hue='species')
plt.plot()
plt.show()
sb.pairplot(data, hue='species')
plt.show()

iris_setosa = data.loc[data['species'] == 'setosa']
plt.plot(iris_setosa['petal length (cm)'], np.zeros_like(iris_setosa['petal length (cm)']),'o', label = 'setosa')
iris_versicolor = data.loc[data['species'] == 'versicolor']
plt.plot(iris_versicolor['petal length (cm)'], np.zeros_like(iris_versicolor['petal length (cm)']),'o', label = 'versicolor')
iris_virginica = data.loc[data['species'] == 'virginica']
plt.plot(iris_virginica['petal length (cm)'], np.zeros_like(iris_virginica['petal length (cm)']),'o', label = 'virginica')
plt.xlabel('petal length')
plt.grid()
plt.legend()
plt.show()

# # sb.FacetGrid(data, hue='species').map(sb.distplot,'petal length (cm)').add_legend()
# # plt.show()
sb.histplot(data=data, hue='species', x='petal length (cm)', kde=True, element='step')
plt.legend()
plt.show()
sb.histplot(data=data, hue='species', x='petal width (cm)', kde=True, element='step')
plt.legend()
plt.show()
sb.histplot(data=data, hue='species', x='sepal length (cm)', kde=True, element='step')
plt.legend()
plt.show()
sb.histplot(data=data, hue='species', x='sepal width (cm)', kde=True, element='step')
plt.legend()
plt.show()

iris_setosa = data.loc[data['species']=='setosa']
count, bin_edges=np.histogram(iris_setosa['petal length (cm)'], bins=10, density=True)
pdf=count/(sum(count))
print(pdf)
print(bin_edges)
cdf=np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, marker='o')
plt.plot(bin_edges[1:], cdf, marker='o')
# plt.plot(bin_edges[1:], pdf, marker='o')
# plt.plot(bin_edges[1:], cdf, marker='o')
# plt.title("PDF of Setosa Petal Length")
# plt.xlabel("Petal Length (cm)")
# plt.ylabel("Probability")
# plt.grid()
# plt.show()

iris_virginica=data.loc[data['species']=='virginica']
counts, bin_edges = np.histogram(iris_virginica['petal length (cm)'], bins=10, density=True)
pdf=counts/(sum(counts))
cdf=np.cumsum(pdf)
print(pdf)
print(bin_edges)
print(cdf)
plt.plot(bin_edges[1:], pdf, marker='o')
plt.plot(bin_edges[1:], cdf, marker='o')

iris_versicolor=data.loc[data['species']=='versicolor']
counts, bin_edges=np.histogram(iris_versicolor['petal length (cm)'], bins=10, density=True)
pdf=counts/(sum(counts))
cdf=np.cumsum(pdf)
plt.plot(bin_edges[1:], pdf, marker='o')
plt.plot(bin_edges[1:], cdf, marker='o')
plt.legend()
plt.title("PDF and CDF of Iris Flower Petal Length")
plt.grid()
plt.show()

data.hist(bins=10, figsize=(10,10), grid=True)
plt.show()
features=data.drop('species', axis =1)
kmeans_model = KMeans(n_clusters=3, random_state=1, n_init=10).fit(features)
labels=kmeans_model.labels_
cluster_sklearn = kmeans_model.cluster_centers_
print(labels)
print(cluster_sklearn)

def plot_clusters_sklearn(data, labels, clusters):
    plt.scatter(data[:,0], data[:,1], c=labels, cmap='viridis', label='Data Points')
    plt.scatter(clusters[:,0], clusters[:,1], s=200, color='red', marker='X', label='Centers')
    plt.legend()
    plt.grid(True)
    plt.show()
plot_clusters_sklearn(features.values, labels, cluster_sklearn)

sse=[]
for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=1, n_init=10).fit(features)
    sse.append(kmeans.inertia_)
plt.plot(range(1, 11), sse, marker='o')
plt.xticks(range(1, 11))
plt.xlabel('Number of Clusters')
plt.ylabel("SSE")
plt.legend()
plt.grid()
plt.show()

