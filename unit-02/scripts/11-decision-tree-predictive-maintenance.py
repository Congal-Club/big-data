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
os.chdir("D://Python/")
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

##CONSTRUCCIÓN DE ÁRBOL DE DECISIÓN


#IMPORTAR LIBRERIAS
#IMPORTAR LIBRERÍA
from sklearn.metrics import f1_score, precision_score, recall_score, confusion_matrix
from sklearn import tree

#mod=tree.
modeloTree = tree.DecisionTreeClassifier(criterion='entropy', min_samples_leaf=1, min_samples_split=2)
modeloTree.fit(x_train,y_train)



# Evaluación 
acc_train_tree= modeloTree.score(x_train,y_train)
acc_test_tree = modeloTree.score(x_test,y_test)
print('acc_train = ', acc_train_tree)
print('acc_test = ', acc_test_tree)

y_pred1=modeloTree.predict(x_test)
y_pred1

p=precision_score(y_test, y_pred1, average=None)
r=recall_score(y_test, y_pred1, average=None)
print(p,r)

f2=f1_score(y_test, y_pred1,average=None)
print(f2)


T=np.mean(p)
Tr=np.mean(r)
print(T,Tr)


promT1=np.mean(f2)
print(promT1)


import seaborn as sns
import matplotlib.pyplot as plt

sns.set()
f1,ax1=plt.subplots()
C22=confusion_matrix(y_test,y_pred1,labels=[0,1,2,3,4,5])
print(C22)
sns.heatmap(C22,annot=True,ax=ax1,cbar=True)
ax1.margins(4,4)
ax1.set_title('matriz de confusion')
ax1.set_xlabel('predecir')
ax1.set_ylabel('true')


# Definición de los datos  para realizar una prueba de clasificación con la 
# máquina de vector soporte.
paciente = np.array([[ 0,0,0,0,0,0,0,0,0]])
diagnostico = modeloTree.predict(paciente)
print(diagnostico)

#Debe indicar la falla 3	
paciente = np.array([[0.9816091954022987,0.9850223072020395,0.9913374913374914,0.06005221932114883,0.5652173913043478,1,0,1,0]])
diagnostico = modeloTree.predict(paciente)
print(diagnostico)

#Debe indicar la falla 3	
paciente=np.array([[0.98128078817734,0.984384958572339,0.5041580041580042,0.5391644908616188,0.8221343873517787,1,0,1,0]])
diagnostico = modeloTree.predict(paciente)
print(diagnostico)
