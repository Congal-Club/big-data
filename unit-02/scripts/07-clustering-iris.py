"""
Created on Fri Mar  5 18:31:42 2021

@author: Cesar

Objetivo de la práctica: Aplicar el algoritmo de 
K-means para realizar clusterización o agrupamiento.
"""

# Obtener datasets de seaborn
import seaborn as sns
sns.get_dataset_names()

df_iris_completo = sns.load_dataset('iris')
df_iris_completo.info()
df_iris_completo.head()
df_iris_completo

# Para aplicar algorimows de k-means, tendríamos que seleccionar las 4 primera variables
df_iris = df_iris_completo[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
df_iris.head(10)
df_iris.info()
df_iris.describe()

# Una forma distinta de graficar la información ver la relación entre las variables.
sns.pairplot(df_iris)

x = df_iris.iloc[:, [0, 1, 2, 3]].values

# Encontrar el valor óptimo de cluster para la clasificación k-means
from sklearn.cluster import KMeans
wcss = [] # Within cluster sum of squares

for i in range(1,11):
    kmeans=KMeans(n_clusters=i, init='k-means++', max_iter=300, n_init=10, random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
    
# Graficando los resultados sobre una línea, permitiendo obervar el punto de quiebre "the elbow"
import matplotlib.pyplot as plt
plt.plot(range(1,11), wcss)
plt.title("El método del codo--The elbow method")
plt.xlabel("Número de clusters")
plt.ylabel("WCSS") # Within cluwter sum of squres
plt.show()

# Aplicando kmeans sobre el datase/Creando el clasificador k-means
kmeans = KMeans(n_clusters=3, init='k-means++', n_init=10, max_iter=300, random_state=0)
y_kmeans = kmeans.fit_predict(x) # y_means tendría la información de ala asignación de cad observación a un cluster determinado

# Visualizando los clusters
plt.scatter(x[y_kmeans==0,0], x[y_kmeans==0,1], s=100, c='red', label="iris-setosa")
plt.scatter(x[y_kmeans==1,0], x[y_kmeans==1,1], s=100, c='blue', label="iris-versicolor")
plt.scatter(x[y_kmeans==2,0], x[y_kmeans==2,1], s=100, c='green', label="iris-virginica") 

# Graficando los centroides del os clusters
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:1], s=100, c='black', label='Centroids')
plt.legend()

# Evaluating the Model
import pandas as pd
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
# ,precision_score,recall_score,classification_repor
# We can check the accuracy score of our model.

y_test = pd.DataFrame(df_iris_completo.iloc[:, [4]].values)

y_test = y_test.replace("setosa", 1)
y_test = y_test.replace("versicolor", 0)
y_test = y_test.replace("virginica", 2)

print("Matriz de confusión")
confusion_matrix(y_kmeans, y_test)

print("Valor de Precisión del clustering")
accuracy_score(y_kmeans, y_test)
