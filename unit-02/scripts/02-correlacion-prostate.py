'''
Análisis de corelación de las tablas

CORRELACIÓN - Medida estadistica para determinar la relación entre dos variables.  
Con que intensidad y de que tipo:
Positiva directa ; indirecta o negativa se mueven en sentido opuesta; 
    independencia estadística cada variable se mueve por su lado.

Coeficiente de correlación de Pearson  o Kendall y  Spearman.
En un rango -1 0 1
'''

# Configurar la carpeta de trabajo
import os
os.chdir("D:\\Python")
os.getcwd()

import pandas as pd
import numpy as np

path_to_file = 'prostate_data.csv'
PDatos=pd.read_csv(path_to_file,delimiter=';')
#PDatos=pd.DataFrame(PDatos)
PDatos.shape
PDatos.columns
PDatos.head()
PDatos.info
PDatos.describe().transpose()
PDatos.dtypes

PDatos['lcavol'] = PDatos['lcavol'].apply(lambda x: x.replace(',','.'))
PDatos['lcavol'] = PDatos['lcavol'].astype(float)
PDatos['lpsa'] = PDatos['lpsa'].apply(lambda x: x.replace(',','.'))
PDatos['lpsa'] = PDatos['lpsa'].astype(float)
PDatos['lweight'] = PDatos['lweight'].apply(lambda x: x.replace(',','.'))
PDatos['lweight'] = PDatos['lweight'].astype(float)
PDatos['lbph'] = PDatos['lbph'].apply(lambda x: x.replace(',','.'))
PDatos['lbph'] = PDatos['lbph'].astype(float)
PDatos['lcp'] = PDatos['lcp'].apply(lambda x: x.replace(',','.'))
PDatos['lcp'] = PDatos['lcp'].astype(float)
PDatos.dtypes


# ANÁLISIS DE CORRELACIÓN ENTRE LAS VARIABLES

# Correlación entre todas la variables
cor_total=PDatos.corr()
print("Correlación entre todas las variables del dataset:  ", cor_total)
cor_total.fill_diagonal=20

#Correlación máxima
Ds_Con_NP=np.matrix(cor_total)
np.fill_diagonal(Ds_Con_NP,0)
print("Valor mayor de correlación " , Ds_Con_NP.max())


# Se elijen las variables cuya correlación sea la o las mayores
co1=PDatos[['lcavol','lpsa']]
co1=pd.DataFrame(co1)
cor1=co1.corr()
print("La correlación entre las variables es: ",cor1)


#Graficando para analizar correlaciones mediante un diagrama de dispersión
import matplotlib.pyplot as plt
plt.scatter(PDatos['lcavol'],PDatos['lpsa'])
plt.title('Relación lcavol y lpsa')
plt.xlabel('Tamaño del tumor lcavol')
plt.ylabel('Antigeno lpsa')

#Graficando para analizar correlaciones mediante un diagrama de dispersión y líneas
plt.plot(PDatos['lcavol'],PDatos['lpsa'])
plt.scatter(PDatos['lcavol'],PDatos['lpsa'])
plt.title('Relación lcavol y lpsa')
plt.xlabel('Tamaño del tumor lcavol')
plt.ylabel('Antigeno lpsa')


#Graficando con diagrmas de dispersión todas las relaciones entre las variables
import seaborn as sns
sns.pairplot(PDatos)






