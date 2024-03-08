'''
# Análisis de corelación de las tablas

CORRELACIÓN - Medida estadistica para determinar la relación entre dos variables.  
Con que intensidad y de que tipo 
Positiva directa , indirecta o negativa se mueven en sentido opuesta, 
independencia estaristica cada variable se mueve por su lado.
Coeficiente de correlaci?n de Pearson
En un rango -1 0 1
'''

#Configurar la carpeta de trabajo
import os
os.chdir("C:\\Python")
os.getcwd()

import pandas as pd

#Creando un diccionario

datos = {'asistencias': [-4.0, 5.0, 5, 6, 7, 8, 8, 10],
        'rebotes': [12, 14, 13, 7, 8, 8, 9, 13],
        'puntos': [22, 24, 26, 26, 29, 32, 20, 14]
        }

df = pd.DataFrame (datos, columns = ['asistencias', 'rebotes', 'puntos'])
df

#crear matriz de correlación
df.corr ()

#crear la misma matriz de correlación con coeficientes redondeados a 3 decimales 
df.corr().round(3)

import seaborn as sns

sns.pairplot(df)
sns.pairplot(df[['asistencias','puntos']])
sns.pairplot(df[['rebotes','puntos']])
