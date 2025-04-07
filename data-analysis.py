import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

iris = pd.read_csv("C:\\Users\\User\\Downloads\\iris.csv")

print(iris.head())
print(iris.shape)
print(iris.columns)
print(iris['variety'].value_counts())
print(iris.info())

#First Plot
plt.plot(iris['variety'])
plt.xlabel("No. of data points")
plt.show()

#Second Plot
plt.hist(iris["variety"],color="green")
plt.show()

print(iris.describe())

sb.set_style('whitegrid')
sb.scatterplot(data=iris, x='sepal.length', y='sepal.width', hue='variety')
plt.show()

sb.set_style('whitegrid')
sb.pairplot(iris, hue='variety', size=3)
plt.show()

sb.FacetGrid(iris,hue="variety").map(sb.distplot,'petal.length').add_legend()
plt.show()