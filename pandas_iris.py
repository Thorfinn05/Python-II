import pandas as pd
iris = pd.read_csv("C:\\Users\\User\\Downloads\\iris.csv")

print(iris)
print(iris.head())
print(iris.describe())
print(iris.sample(10))