# -*- coding: utf-8 -*-
"""

1. Usando el módulo csv de la librería estándar
Para extraer los datos de un fichero csv, primero lo «abrimos» con la función open(). Después, usamos 
la función, csv.reader(), que lee línea a línea el fichero, y hace una lista de todas las columnas en el
 objeto reader. Es mucho más sencillo hacerlo que explicarlo, así que mejor, lo vemos con un ejemplo.
Hemos guardado, en nuestro directorio de trabajo, un dataset de ejemplo con datos sobre diabetes.

"""
#Configurar la carpeta de trabajo
import os
os.chdir("C:\\Python")
os.getcwd()

import csv
f= open("diabetes.csv")
reader = csv.reader(f)
for row in reader:
    print (row) 


'''
2. Usando NumPy
Otra forma de cargar los datos es usando la función numpy.loadtxt()  de la librería NumPy. 
Para ello, lo primero que tendremos que hacer es cargar la librería.
Esta función asume que el fichero no tiene cabeceras, y que todos los datos tienen el mismo formato. 
Como no es el caso de nuestro dataset sobre diabetes, usaremos el modificador «skiprow» para indicar que 
no debe tener en cuenta la primera fila.
En este ejemplo, también le hemos pedido que nos indique las dimensiones del dataset y nos muestre los datos.

'''
#REVISAR ESTE BLOQUE DE CÓDIGO
import numpy
filename = 'diabetes.csv'
raw_data = open(filename)
data = numpy.loadtxt(raw_data, delimiter=",",skiprows=1)
print(data.shape)
print(data)

'''
3. Usando Pandas
Esta tercera forma de cargar los datos es, probablemente, 
la más popular entre los científicos de datos como veremos, por muy buenas razones. 
En este caso, la función que usaremos es readcsv(). Esta función nos ofrece una gran flexibilidad a la 
hora de importar datos, ya que de forma automática, o con una simple línea de comando, permite hacer cosas 
como:
Detectar automáticamente las cabeceras o «headers»
«Saltar» líneas con el modificador «skiprow«
Detectar automáticamente el tipo de datos (número entero, decimal, cadena de texto etc)
Identificar campos con datos erróneos o vacíos
Convertir los datos en formato csv en un dataframe de Pandas
Los dataframes de Pandas son unas estructuras de datos diseñadas especialmente para facilitar el trabajo 
del analista y científico de datos. Permiten trabajar con datos de todo tipo (enteros, decimales, cadenas
de texto) dispuestos en forma de tablas, incluso con series temporales.
También se pueden usar como vectores y matrices, lo que permite realizar operaciones de álgebra lineal, 
como la multiplicación de matrices.
Otro aspecto importante de pandas.read_csv() es que puede ejecutarse con la opción chunksize, que, en 
lugar de cargar el fichero de datos completo en memoria, permite hacerlo en fragmentos (chunks) de tamaño
 configurable, mejorando mucho la eficiencia en la carga de datos de ficheros muy grandes.

'''

import pandas
filename = 'diabetes.csv'
data = pandas.read_csv(filename, header=0)
print(data.shape)
print (data.head(10))


"""
4. Desde URL.
Otra de las formas más habituales de cargar un dataset es directamente desde la URL donde se alojan 
los datos. Este método es perfectamente compatible con los anteriores. Por ejemplo, podemos modificar 
el ejemplo anterior, para que cargue los datos desde su ubicación original.

"""

import pandas
url = "https://datahub.io/machine-learning/diabetes/r/diabetes.csv"
data = pandas.read_csv(url)
print(data)

# En Pandas, el modificador tail nos ofrece una vista de los datos mucho más atractiva
# Ver final
data.tail()


'''
5. Desde otras librerías.
Cuando lo que queremos es hacer una prueba rápida, nos pueden resultar muy útiles los datasets que traen 
«de serie» algunos de los paquetes más populares como statsmodels, scikit-learn, o seaborn. Se trata de
 conjuntos de datos de todo tipo «para hacer pruebas» que se conocen como «Toy datasets» y de los que 
 hablaremos con más detalle en el próximo post.

'''