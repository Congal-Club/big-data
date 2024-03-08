# -*- coding: utf-8 -*-
"""


@author: Elvia

Como realizar una regresión lineal 
y=ax+b
a y b son calculada por los algoritmos, solo damos x y se nos regresaría y.

Unión de dos datos x +y, se ve como oun punto en un plano xy.
"""

# Importar librerias de vectores
import numpy as np
import pandas as pd
# matplotlib es para graficar
import matplotlib.pyplot as plt



#Configurar el directorio de trabajo
import os
os.chdir("D:\\Python/")
os.getcwd()
datos="prostate_data.csv"
df=pd.read_csv(datos,delimiter=";")

df.shape
df.info
df.columns
df.dtypes

df['lcavol'] = df['lcavol'].apply(lambda x: x.replace(',','.'))
df['lcavol'] = df['lcavol'].astype(float)
df['lpsa'] = df['lpsa'].apply(lambda x: x.replace(',','.'))
df['lpsa'] = df['lpsa'].astype(float)
df.dtypes

#df=pd.r
#ead_excel("example.xlsx",sheet_name="example")
#newprostate_data
#Convertir a Data Frame
#df=pd.DataFrame(df)
##Y=AX + B ##  X variable independiente, Y es la variable dependiente.
#X=df["lpsa"]
#Y=df["lpsa"]
X=np.array(df[["lcavol"]])
Y=np.array(df[["lpsa"]])



#Graficar los datos (Gráficos de dispersión)
plt.scatter(X,Y)
#plt.plot(X,Y)
plt.xlabel("Variable lcavol-Variable predictora")
plt.ylabel("Variable lpsa- Variable objetivo o tarjet")
plt.title("Relación entre variables para predecir cancer de prostata")
plt.show()

#Herramienta de python para realizar regresión lineal
from sklearn import linear_model
#Los datos se dividen en 80% entrenamiento y 20% de prueba
from sklearn.model_selection import train_test_split

#Se dividen los datos en entrnamiento(datos de entrada y salida) y prueba(entrada y salida).
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.20)

#Realizar la regresión
regresion=linear_model.LinearRegression()

#Inicia el algorito para aprender
regresion.fit(X_train,Y_train)

#Imprimir el score para saber que tan bueno es el modelo generado
print("Precisión del modelo: ")
print(regresion.score(X_train,Y_train))

#Evaluo los datos de prueba en el modelo creado, predecir Y en base a X.
Y_pred=regresion.predict(X_test)

plt.scatter(X_train,Y_train)
plt.scatter(X_test,Y_pred, color='red')
plt.plot(X_test,Y_pred, color="red",linewidth=3)
plt.title("Regresion Lineal Simple")
plt.xlabel("lcavol")
plt.ylabel("lpsa")
plt.show()


print("Ecuación de la regresión: ")
print("Y=",regresion.coef_,"X + ",regresion.intercept_)
