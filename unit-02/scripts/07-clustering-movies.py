"""
Objetivo de la práctica: Aplicar el algoritmo de 
K-means para realizar clusterización o agrupamiento.

"""

import numpy as np
import pandas as pd
# matplotlib es para graficar
import matplotlib.pyplot as plt

#Herramienta de python para realizar regresiones y clasificación entre otras
##SciKtitLearn 
from sklearn.cluster import KMeans
#Extraer datasets
datos=pd.read_csv("C:/Users/cesar/OneDrive/Documentos/ITA/Octavo Semestre/Big Data Analytics/Unidad II/Materiales y Recursos/Scripts Python/movies.csv",sep=';')
#datos=pd.read_csv("D:Python/movies.csv")
df=pd.DataFrame(datos)
df.columns

#EXPORTAR DATOS A ARCHIVPS EXCEL Y CSV
#datos.to_excel('C:/Python/datos_excel.xlsx',index=False)
#EXPORTAR DF A CSV
#datos.to_csv('C:/Python/datos_csv.csv',index=False,sep=';')


# Realizar la clusterización del dataframe

x=df["cast_total_facebook_likes"].values
y=df["imdb_score"].values


#Obtener valores estadísticos del dataframew: valor máximo, mínimo y promedio
print("Valor máximo de likes: ",df["cast_total_facebook_likes"].max())
print("Valor mínimo de likes: ",df["cast_total_facebook_likes"].min())
print("Valor promedio que tienen las paliculas: ",df["cast_total_facebook_likes"].mean())

# Para la agrupación se deben tener los datos en una matriz o arreglo.
info=df[["cast_total_facebook_likes","imdb_score"]]
#info=df[["cast_total_facebook_likes","imdb_score"]].as_matrix()
print(info)
    #Otra forma de hacerlo, Normalmente se usa X e Y
X=np.array(list(zip(x,y)))  #Otra forma de tener los datos como lista
print(X)

#Determinar la cantidad de clusters o grupos que generaremos

kmeans=KMeans(n_clusters=3)#Clusteriza los datos en 2,3 ó 4.
kmeans=kmeans.fit(X)   #Se asignana etiquetas a los datos en análisis.
labels=kmeans.predict(X) #Etiquetando los datos..distancia menor entre los vecinos.
centroids=kmeans.cluster_centers_  # Muestra donde se asignaron los centroides de manera aleatoria
centroids

#Visualizarlo los datos y la clusterization en una gráfica
colors=["m.","r.","c.","y.","b."]

for i in range(len(X)):
    print("Coordenada: ",X[i],"Label: ",labels[i])
    plt.plot(X[i][0],X[i][1], colors[labels[i]],markersize=10)

#Graficar los centroides
plt.scatter(centroids[:,0],centroids[:,1],marker="X",s=50,linewidths=2,zorder=10)
plt.show()
