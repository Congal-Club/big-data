# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 14:40:28 2023

@author: elvia
"""

# PREPROCESAMIENTO DE LOS DATOS 
import pandas as pd                                   # Librería para manejo de datos y archivos.
import numpy as np                                    # Librería para operaciones matemáticas.
from sklearn.model_selection import train_test_split  # Librería para construir conjuntos de entrenamiento y prueba.

# Lectura del archivo de datos.
import os
os.chdir("C://Python/")
os.getcwd()
dataset = pd.read_csv('predictive_maintenance.csv')
dataset.head()
dataset.shape
dataset.info()

# RegiStros de  fallas
datasetCR = dataset[dataset['Failure Type']=='Heat Dissipation Failure']
datasetCR
datasetCR.shape

# De la tabla original se eliminará las primeras columnas.
dataset.info()
dataset1 = dataset.drop(['UDI','Product ID'], axis = 1)
dataset1.head()
dataset1.info()

## Codificación 1-hot de variables temporales
variables_ficticias = ['Type']
for variable in variables_ficticias:
    dummies = pd.get_dummies(dataset1[variable], prefix=variable, drop_first=False)
    dataset1 = pd.concat([dataset1, dummies], axis=1)
dataset1.head()

# Removemos variables temporales
dataset1 = dataset1.drop(['Type'], axis=1)
dataset1.head()

# Creación de diccionario
mapeo= {'No Failure':0,'Heat Dissipation Failure':1,'Overstrain Failure':2,'Power Failure':3,'Random Failures':4,'Tool Wear Failure':5}
dataset1= dataset1.replace({'Failure Type': mapeo})
dataset1

#Normalizacion
dataset1['Air temperature [K]'] = dataset1['Air temperature [K]']/dataset1['Air temperature [K]'].max()
dataset1['Process temperature [K]'] = dataset1['Process temperature [K]']/dataset1['Process temperature [K]'].max()
dataset1['Rotational speed [rpm]'] = dataset1['Rotational speed [rpm]']/dataset1['Rotational speed [rpm]'].max()
dataset1['Torque [Nm]'] = dataset1['Torque [Nm]']/dataset1['Torque [Nm]'].max()
dataset1['Tool wear [min]'] = dataset1['Tool wear [min]']/dataset1['Tool wear [min]'].max()
dataset1['Target'] = dataset1['Target']/dataset1['Target'].max()
dataset1.head()

# Separación de las características y las variables objetivo
caracteristicas = dataset1.drop(['Failure Type'],axis=1)
targets = dataset1['Failure Type']

# Construcción de los conjuntos de entrenamiento y prueba.
x_train, x_test, y_train, y_test = train_test_split(caracteristicas, targets,test_size = 0.20,random_state = 10)

# verificación del tamaño de los conjuntos de train y test
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

##CONSTRUCCIÓN DE MÁQUINA DE SOPORTE VECTORIAL


#IMPORTAR LIBRERIAS
from sklearn import svm
from sklearn.metrics import f1_score, precision_score, recall_score

modeloSVM = svm.SVC(C=25, kernel='rbf', gamma=100 ,probability=True)
#MOD=svm.SVC(C=5, kernel='poly',grade=)
modeloSVM.fit(x_train, y_train)

acc_train = modeloSVM.score(x_train, y_train)
acc_test = modeloSVM.score(x_test, y_test)
print('acc_train = ', acc_train)
print('acc_test = ', acc_test)

y_pred=modeloSVM.predict(x_test)
y_pred

p=precision_score(y_test, y_pred, average=None)
r=recall_score(y_test, y_pred, average=None)
print(p,r)

f1=f1_score(y_test, y_pred,average=None)
print(f1)

T=np.mean(p)
Tr=np.mean(r)
print(T,Tr)

promT=np.mean(f1)
print(promT)


#matriz de confusion
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt                 # Librería para graficar

sns.set()
f,ax=plt.subplots()
C2=confusion_matrix(y_test,y_pred,labels=[0,1,2,3,4,5])
print(C2)
sns.heatmap(C2,annot=True,ax=ax,cbar=True)
ax.margins(4,4)
ax.set_title('matriz de confusion')
ax.set_xlabel('predecir')
ax.set_ylabel('true')

# Definición de los datos  para realizar una prueba de clasificación con la 
# máquina de vector soporte.
paciente = np.array([[ 0,0,0,0,0,0,0,0,0]])
diagnostico = modeloSVM.predict(paciente)
print(diagnostico)

	
paciente = np.array([[0.9816091954022987,0.9850223072020395,0.9913374913374914,0.06005221932114883,0.5652173913043478,1,0,1,0]])
diagnostico = modeloSVM.predict(paciente)
print(diagnostico)

	
[[0.98128078817734,0.984384958572339,0.5041580041580042	0.5391644908616188	0.8221343873517787	1.0	5	0	1	0

