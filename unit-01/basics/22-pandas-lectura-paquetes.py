# Obtener datasets de seaborn
import seaborn as sns

sns.get_dataset_names()

df_iris = sns.load_dataset('iris')
df_iris.head()
df_iris

# Obtener datasets de sklearn
from sklearn.datasets import fetch_california_housing
housing = fetch_california_housing()

housing.data
housing.data.shape
housing.feature_names
housing.target
housing.target.shape

# Convirtiendo a una DataFrae de pandas
import pandas as pd
import numpy as np

df_housing = pd.DataFrame(housing.data, columns=housing.feature_names)
df_housing.head()

df_housing.columns
target = pd.Series(housing.target)
target

'''
#Para renombrar índices de un dataframe
df.rename(index={0:'Index1',1:'Index2'}, inplace=True) #Renombrar o cambiar el nombre de los índices.
df.head()
'''
