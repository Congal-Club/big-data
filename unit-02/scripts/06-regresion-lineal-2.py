# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 17:39:11 2021

@author: Elvia
"""

import numpy as np
import pandas as pd

# matplotlib es para graficar

import matplotlib.pyplot as plt

#Herramienta de python para realizar regresiones y clasificación entre otras
##SciKtitLearn 

from sklearn import linear_model

#La parte para sacar la R cuadrada, que tan cercanos están los valores predecidos a los reales
from sklearn.metrics import r2_score
regr=linear_model.LinearRegression()

#Extraer datasets


# Importing urlib (BigGorilla's recommendation for data acquisition from the web)
import urllib.request
import os

# Creating the data folder
if not os.path.exists('./data'):
    os.makedirs('./data')
    
    # Obtaining the dataset using the url that hosts it
kaggle_url = 'https://github.com/sundeepblue/movie_rating_prediction/raw/master/movie_metadata.csv'
if not os.path.exists('./data/kaggle_dataset.csv'):     # avoid downloading if the file exists
    response = urllib.request.urlretrieve(kaggle_url, './data/kaggle_dataset.csv')


os.chdir("C:\\Python/data")
os.getcwd()
datos=pd.read_csv("kaggle_dataset.csv")
df=pd.DataFrame(datos)

#X e Y
x=df["movie_facebook_likes"]
y=df["imdb_score"]

X=x[:,np.newaxis]  #Le está dando el formato a los datos de un arreglo
print(X)


#Realizar el modelo y la predicción
print(regr.fit(X,y))
print(regr.coef_)

m=regr.coef_[0]  #m es la pendiente
b=regr.intercept_ #b Interseccion
y_p=m*X+b   #Valor que se predice

#Formato de ecuación
print("y={0} * x+1{1}".format(m,b))

print(regr.predict(X)[0:5])

#Como se pueden apreciar los datos en una gráfica

import matplotlib.pyplot as plt

print("El valor de R2: ",r2_score(y,y_p)) #Se compara con el valor real de Y

plt.scatter(x,y,color="blue")
plt.plot(x,y_p,color="red")
plt.title("Regresión Lineal",fontsize=16)
plt.xlabel("Likes de Facebook",fontsize=13)
plt.ylabel("Calificación IMDB Score",fontsize=13)




