import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.datasets import load_diabetes

diab = load_diabetes()
data = pd.DataFrame(diab.data, columns=diab.feature_names)
print(data)
data['target']=diab.target
print(data['target'])

print(data.head())
print(data.shape)
print(data['target'])
print(data.describe())

key_features=['age', 'sex', 's3']
data[key_features].hist(bins=20, figsize=(10,10), grid=True)
plt.show()

data.hist(bins=20, figsize=(10,10), grid=True)
plt.show()

sb.set_style('whitegrid')
sb.pairplot(data, size=3)
plt.show()
