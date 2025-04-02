import pandas as pd
iris = pd.read_csv("C:\\Users\\User\\Downloads\\iris.csv")

print(iris)
print(iris.head())
print(iris.describe())
print(iris.sample(10))
print(iris.columns)
print(len(iris.columns))
print(iris.shape)
print(iris.iloc[5:11])
print(iris[["petal.length", "petal.width"]])
print(iris['variety'].value_counts())
print(iris[iris['variety']=='Setosa'])
print(iris['petal.length'].sum())
print(iris['petal.length'].mean())
print(iris['petal.length'].mode())
print(iris['petal.length'].max())
print(iris['petal.length'].min())
# iris['total_value']==iris.sum(axis=1)
# print(iris.head())
iris.rename(columns={"sepal.width":'SepalWidthCm', 'petal.width':'PetalWidthCm'},inplace=True)
print(iris.columns)