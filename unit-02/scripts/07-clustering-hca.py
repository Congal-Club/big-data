import pandas as pd

# Sustituir el path_to_file por el path de la ubicación donde se encuentra el archivo shopping-data.csv
path_to_file = 'C:/Users/cesar/OneDrive/Documentos/ITA/Octavo Semestre/Big Data Analytics/Unidad II/Materiales y Recursos/Scripts Python/shopping-data.csv'
customer_data = pd.read_csv(path_to_file)

#Muestra ladimensiones del dataset
customer_data.shape

#Muestra las variables del dataset
customer_data.columns
customer_data.info()

#Exploración de los datos 
Score_max=customer_data['Spending Score (1-100)'].max() #Pueden cambiar la función para explorar los atos max, mean, sd ,etc.
Score_max
Score_min=customer_data['Spending Score (1-100)'].min() #Pueden cambiar la función para explorar los atos max, mean, sd ,etc.
Score_min
Score_mean=customer_data['Spending Score (1-100)'].mean() #Pueden cambiar la función para explorar los atos max, mean, sd ,etc.
Score_mean
Score_median=customer_data['Spending Score (1-100)'].median() #Pueden cambiar la función para explorar los atos max, mean, sd ,etc.
Score_median
Score_var=customer_data['Spending Score (1-100)'].var() #Pueden cambiar la función para explorar los atos max, mean, sd ,etc.
Score_var
Score_std=customer_data['Spending Score (1-100)'].std() #Pueden cambiar la función para explorar los atos max, mean, sd ,etc.
Score_std

#Exploración de los datos- obteniendo conclusiones
customer_data['Spending Score (1-100)'].hist()
# transpose() transpone la tabla, para facilitar la comparación entre los valores
Guarda_Estadisticas=customer_data.describe().transpose()
#Para todas las features, la media(mean) se encuentra lejos de la desviacion estándar
# lo que indica que nuestros datos tiene una alta variabilidad.
'''
The variability and the size of the data are important in clustering 
analysis because distance measurements of 
most clustering algorithms are sensitive to data magnitudes.
'''
#Esplorar con pandas para analizar si los tipos datos estas completos o tiene valores nulos
customer_data.info()

#Podemos ver que "Genre" es una variable categoria, si deseamos agregarla al modelo hay que transformarla
# en un valor numérico
customer_data.head() #Dos categorias, Male and Female
customer_data['Genre'].unique() #Visualizo todas los posibles valores de la variable categorica
# Transformamos la variable categórica 1-Female, 0- Male pero antes checamos que tan balanceados están los géneros
customer_data['Genre'].value_counts()
customer_data['Genre'].value_counts(normalize=True)

#Si consideramos la edad para el modelo también hay que tratar los datos, se segmenta(categoriza) por edades

#CODIFICANDO VARIABLES E INGENIERÍA DE CARACTERÍSTICAS

#Creando categorías que varían de 10 en 10, 20-30, 30-40, 40-50 y así sucecivamente
intervals = [15, 20, 30, 40, 50, 60, 70]
col = customer_data['Age']
customer_data['Age Groups'] = pd.cut(x=col, bins=intervals)

# Visualizar el resultado almacenado en la variable
customer_data['Age Groups'].head() #Mostrar solo algunos o todos según se requiera.

#Podemos calcular cuantos consumidores tenemos en cada categoría

customer_data.groupby('Age Groups')['Age Groups'].count()


#OTRA MANERA DE TRATAR LOS DATOS 
#There are many different ways of making that transformation -
# we will use the Pandas get_dummies() method that creates a new column
# for each interval and genre and then fill its values with 0s and 1s- this kind of
# operation is called one-hot encoding. Let's see how it looks:
    
   
# The _oh means one-hot
customer_data_oh = pd.get_dummies(customer_data)
# Display the one-hot encoded dataframe
customer_data_oh 
customer_data_oh.columns

#Basic Plotting and Dimensionality Reduction
import seaborn as sns

# Dropping CustomerID column from data 
customer_data = customer_data.drop('CustomerID', axis=1)

sns.pairplot(customer_data)

#Como se observa la elación entre Annual Income y Spending Score 1-100 están muy corelacionadas
# y formas agrupaciones más visibles.
sns.scatterplot(x=customer_data['Annual Income (k$)'],
                y=customer_data['Spending Score (1-100)'])# Se identifican 5 grupos a simple vista

#Plotting Data After Using PCA
'''
It can be useful when we can't plot the data because it has too many dimensions, 
or when there are no data concentrations or clear separation in groups. 
When those situations occur, it's recommended to try reducing data dimensions
 with a method called Principal Component Analysis (PCA).
'''
'''
PCA will reduce the dimensions of our data while trying to preserve as much of its 
information as possible. Let's first get an idea about how PCA works, 
and then we can choose how many data dimensions we will reduce our data to.
Those results are then organized into a matrix, obtaining a covariance matrix.
After getting the covariance matrix, PCA tries to find a linear combination 
of features that best explains it - it fits linear models until it identifies 
the one that explains the maximum amount of variance.
'''

customer_data_oh = customer_data_oh.drop(['Age'], axis=1)
#customer_data_oh = customer_data_oh.drop(['CustomerID'], axis=1)
customer_data_oh.shape # (200, 10)

#IMPORTANDO EL PAQUETA PCA para el análisis de componente principales(Principal Component Analysis)
from sklearn.decomposition import PCA

pca = PCA(n_components=10)
pca.fit_transform(customer_data_oh)
pca.explained_variance_ratio_.cumsum()# Los valores explican la varianza.

#AHORA CON DOS COMPONENTES
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
pcs = pca.fit_transform(customer_data_oh)

pc1_values = pcs[:,0]
pc2_values = pcs[:,1]
sns.scatterplot(x=pc1_values, y=pc2_values)

#Visualizing Hierarchical Structure with Dendrograms
'''
but there's also another way to visualize the relationships
 between our points and help determine the number of clusters
 - by creating a dendrogram (commonly misspelled as dendogram).
 Dendro means tree in Latin.
'''

import scipy.cluster.hierarchy as shc
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 7))
plt.title("Customers Dendrogram")

# Selecting Annual Income and Spending Scores by index
selected_data = customer_data_oh.iloc[:, 1:3]
clusters = shc.linkage(selected_data, 
            method='ward', 
            metric="euclidean")
shc.dendrogram(Z=clusters)
plt.show()

plt.figure(figsize=(10, 7))
plt.title("Customers Dendogram with line")
clusters = shc.linkage(selected_data, 
            method='ward', 
            metric="euclidean")
shc.dendrogram(clusters)
plt.axhline(y = 125, color = 'r', linestyle = '-')
'''

After locating the horizontal line, we count how many times our
 vertical lines were crossed by it - in this example, 5 times. 
 So 5 seems a good indication of the number of clusters that have 
 the most distance between them.
'''

from sklearn.cluster import AgglomerativeClustering

clustering_model = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
clustering_model.fit(selected_data)
clustering_model.labels_

data_labels = clustering_model.labels_
sns.scatterplot(x='Annual Income (k$)',
                y='Spending Score (1-100)',
                data=selected_data,
                hue=data_labels,palette="rainbow").set_title('Labeled Customer Data')
#sns.scatterplot(x='Annual Income (k$)',y='Spending Score (1-100)',data=selected_data,hue=data_labels,pallete='rainbow').set_title('Labeled Customer Data')


clustering_model_pca = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
clustering_model_pca.fit(pcs)

data_labels_pca = clustering_model_pca.labels_

sns.scatterplot(x=pc1_values, 
                y=pc2_values,
                hue=data_labels_pca,
                palette="rainbow").set_title('Labeled Customer Data Reduced with PCA')

#ASIGNAR LAS ETIQUETAS AL DATA SET PRINCIPAL
customer_data['Labels']=data_labels
customer_data_final=customer_data
customer_data['Age Groups'] = pd.cut(x=col, bins=intervals)
