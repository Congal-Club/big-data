'''
    Estadísticas sobre datos.
'''
import pandas as pd
import numpy as np  

#Crear un diccionario ----se llama a numpy porque se creará un diccionario solo con dos columnas.
#Numpy para generar un valor nulo y muestre los datos que estoy analizando.

dic_alumnos={"nombre":["Javier","Marta","Lucia","Pedro","Juan","María"],"Evaluacion Matemáticas":[5,7,8,4,10,np.NaN],"Evaluacion Idiomas":[8,9,7,5,8,6]}
df_alumnos=pd.DataFrame(dic_alumnos)
print(df_alumnos)

#-------------Métodos / Atributo---------------
#Los métodos usan argumento y los atributos solo se usa punto.

# .head(i)- Visualizar los i registros del dateframe. Método.
print(df_alumnos.head(2))

# .shape - devuelve el número de filas y columnas. Atributo
print("Número de filas y columbnas: ", df_alumnos.shape)

# .index - Es un atributo que devuelve la información del índice del dataframe.
print("Índice:",df_alumnos.index,"  Todo va bien")

# .columns - Atributo que devuelve la información de columnas del dataframe.
print("Columnas: ",df_alumnos.columns)

# info()- Método que devuelve información para todas las columnas del dataframe.
print("Información:",df_alumnos.info())

# count- devuelve el númer  de valor Non-Null
print("Valores Non-Null:", df_alumnos.count())


'''
Lo ideal es que utilicemos estos primeros métodos y atributos 
para tener una idea de como es nuestro DataFrame y que información
contiene.
'''


#---------Información Estadística--------------

# sum()  - suma los valores de una columna
print("Suma valores de matemática", df_alumnos["Evaluacion Matemáticas"].sum())

# mean()  - Calcula el promedio de un conjunto de valores.
print("Promedio de matemáticas: ",df_alumnos["Evaluacion Matemáticas"].mean())

# median()- Calcula la mediana de una columna o conjunto de valores numéricos.
print("Mediana: ",df_alumnos["Evaluacion Matemáticas"].median())

# Quantile(k) - calcula el percentil k de una columna.
print("Percentil: ",df_alumnos["Evaluacion Matemáticas"].quantile(0.8))
# El 80% se los lunos con 8.4

# min()- Obtiene el valor mínimo de un conjunto de datos o columna.
print("Valor mínimo: ",df_alumnos["Evaluacion Matemáticas"].min())

# max()- Obtiene el valor máximo de un conjunto sde datos o columna.
print("Valor máximo: ",df_alumnos["Evaluacion Matemáticas"].max())


# descfibe() - Realiza un resumen estadístico para todas las columnas de tipo número de un dataframe.
print("----Descripción------:",df_alumnos.describe())
print(df_alumnos.describe())