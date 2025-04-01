import pandas as pd
iris = pd.read_csv("C:\\Users\\User\\Downloads\\iris.csv")

print(iris)
print(iris.head())
print(iris.describe())
print(iris.sample(10))
print(iris.columns)
print(len(iris.columns))
print(iris.shape)
print(iris.iloc[5,11])