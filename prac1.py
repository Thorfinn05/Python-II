import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

iris = pd.read_csv("C:\\Users\\User\\Downloads\\iris.csv")

print(iris.head())
print(iris.shape)
print(iris.tail())
print(iris.columns)
print(iris['variety'].value_counts())
print(iris.info())

plt.plot(iris['variety'])
plt.xlabel("No. of data points")
plt.show()

plt.hist(iris['variety'], color='purple')
plt.show()

key = ['petal.length', 'petal.width', 'sepal.length']
iris[key].hist(color='green', figsize=(12,4), grid=True, bins=20)
plt.show()

print(iris.describe())

sb.set_style('whitegrid')
sb.pairplot(iris, hue='variety', size=3)
plt.show()

# sb.set_style('whitegrid')
# sb.pairplot(iris)
# plt.plot()
# plt.show()

sb.set_style('whitegrid')
sb.scatterplot(data=iris, x='sepal.length', y='sepal.width', hue='variety')
plt.plot()
plt.show()

iris_setosa = iris.loc[iris['variety'] == 'Setosa']
iris_versicolor = iris.loc[iris['variety'] == 'Versicolor']
iris_virginica = iris.loc[iris['variety'] == 'Virginica']

plt.plot(iris_setosa['petal.length'], np.zeros_like(iris_setosa['petal.length']), 'o', label='Setosa')
plt.plot(iris_versicolor['petal.length'], np.zeros_like(iris_versicolor['petal.length']), 'o', label='Versicolor')
plt.plot(iris_virginica['petal.length'], np.zeros_like(iris_virginica['petal.length']), 'o', label='Virginica')

plt.xlabel('petal.length')
# plt.grid()
plt.legend()
plt.show()

sb.FacetGrid(iris, hue='variety').map(sb.distplot, 'petal.length').add_legend()
plt.show()

counts, bin_edges=np.histogram(iris_setosa['petal.length'], bins=10, density=True)
pdf = counts/(sum(counts))
print(pdf)
print(bin_edges)

cdf = np.cumsum(pdf)
print(cdf)

plt.plot(bin_edges[1:],pdf, label='pdf')
plt.plot(bin_edges[1:], cdf, label='cdf')
plt.legend()
plt.show()