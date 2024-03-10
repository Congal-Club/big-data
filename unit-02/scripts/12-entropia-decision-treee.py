# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 12:35:12 2023

@author: Podriamos guiarnos en 
https://www.youtube.com/watch?v=z5rmY-LV7ME

El data set se descargo de 

https://aprendeconalf.es/estadistica-practicas-r/02-preprocesamiento-datos.html

"""

from scipy.stats import entropy
from math import log
import pandas as pd


#PROMEDIO DE INFORMACIÓN ALMACENADA EN UNA VARIABLE ALEATORIA
# Ejemplo para explicar log
print(log(8,2))
#El resultado representa el número de veces que debo multiplicar 2 para generar el 8
#El logaritmo nos permite calcular el número que requerimos pare reprwsentar un valor cualquiera en binario, sería el resultado del logaritmo más uno. 
#En este caso se requiere 3+1 bits para representar 8

#Ahora se debe entender qué es una variable aleatoria
# Sería aquella que tiene cierta probabilidad de que ocurra, como es el caso de lanzar una moneda bien balanceada, .50 de caer en un lado y .50 de caer en el otro lado.

print(entropy([1/2,1/2],base=2))

#Un nivel de entropia de 1

# Si se tiene una moneda un poco cesgada que sucedería?
print(entropy([6/10,4/10],base=2))   # La entropía se reduce, es que hay menos información par
print(entropy([10/10,0/10],base=2))   # La entropía es cero, ya no hay más información dentro de la variable aleatoria.


#Ahora en un contexto real

edades=pd.Series([40,30,20,50])
colesterol=pd.Series([100,110,100,110])

print(edades.value_counts()/edades.size)
print(colesterol.value_counts()/colesterol.size)
print(entropy(edades.value_counts()/edades.size,base=2))  # Hay mas caos con esta variable, se usa para seleccionar los datos.Hay diferntes valores o medida del casos a la entroía.
print(entropy(colesterol.value_counts()/colesterol.size,base=2))
'''

El resultado indica que es más probable saber que saldrá un paciente con nivel de colesterol o 100 
ó 110 que tener más certidumbre de qué edad saldrán, hay mas casos en la variable edad que en el nivel de colesterol.
'''


"""

#Jugando un poco donde las edades se parezcan

edades=pd.Series([40,30,20,50])
colesterol=pd.Series([100,110,100,110])

print(edades.value_counts()/edades.size)
print(colesterol.value_counts()/colesterol.size)
print(entropy(edades.value_counts()/edades.size,base=2))  # Hay mas caos con esta variable, se usa para seleccionar los datos.Hay diferntes valores o medida del casos a la entroía.
print(entropy(colesterol.value_counts()/colesterol.size,base=2))
"""


#crear nuestros arboles de decición
#Datos de entrenamiento y prueba


#IMPORTAR EL DATA SET DE pacientes

import pandas as pd
import matplotlib.pyplot as plt

#Importando datos
pacientes=pd.read_csv("D:\Python\heart.csv")
saludables=pacientes[pacientes["output"]==0]
cardiacos=pacientes[pacientes["output"]==1]


plt.figure(figsize=(6,6))
plt.xlabel('age',fontsize=20.0)
plt.ylabel('chol',fontsize=20.0)
plt.scatter(saludables["age"],saludables["chol"],
            label="Saludable(Clase:0)",marker='*',c="skyblue",s=200)
plt.scatter(cardiacos["age"],cardiacos["chol"],
            label="Crdiado (Clase: 1)",marker="*",c="lightcoral",s=200)
plt.legend(bbox_to_anchor=(1,0.15))
plt.show()



from sklearn.model_selection import train_test_split

datos_entrena,datos_prueba,clase_entrena,clase_prueba=train_test_split(pacientes[["age","chol"]],
                                                                       pacientes["output"],
                                                                       test_size=0.30)


#Crear el arbol de deciisón
from sklearn import tree
arbol_decision=tree.DecisionTreeClassifier(criterion='entropy',max_depth=3 )
#arbol_decision=tree.DecisionTreeClassifier(criterion="entroppy" )#Podemos crer árboles con diferntes profundidades y diferente 
# Cuando se no se define el npumero de ramas puede sobreentrenar o sobreajusta el modelo

arbol=arbol_decision.fit(datos_entrena,clase_entrena)

#Medi que tan bueno es el modelo, se mide con accuracy--que tantas instancias clasificó correctamente

accuracy=arbol_decision.score(datos_prueba,clase_prueba)
print(accuracy)

print(tree.export_text(arbol,
                       feature_names=["Edad(Age)","Colesterol(Chol)"]))
plt.figure(figsize=(12,6))
tree.plot_tree(arbol,
               feature_names=["Edad(Age)","Colesterol(Chol)"])

plt.show()


#CLASIFICAR A NUEVOS PACIENTES
print("Nuevo Paciente",arbol_decision.predict([[10,350]]))





