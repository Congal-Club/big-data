"""
1. Usando el módulo csv de la librería estándar
Para extraer los datos de un fichero csv, primero lo «abrimos» con la función open(). Después, usamos 
la función, csv.reader(), que lee línea a línea el fichero, y hace una lista de todas las columnas en el
 objeto reader. Es mucho más sencillo hacerlo que explicarlo, así que mejor, lo vemos con un ejemplo.
Hemos guardado, en nuestro directorio de trabajo, un dataset de ejemplo con datos sobre diabetes.
"""

# Configurar la carpeta de trabajo
import os
os.chdir("D:\\Python")
os.getcwd()

import csv
f= open("diabetes2.csv")
reader = csv.reader(f) # Me genera una lista

for row in reader: #Los valores de la lista se muestran de la siguiente manera
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
import numpy
filename = 'diabetes2.csv'
raw_data = open(filename)
data = numpy.loadtxt(raw_data, delimiter=",",skiprows=1)
print(data.shape)
print(data)




#NUEVO CÓDIGO AGREGADO
import pandas as pd
df_diabetes=pd.DataFrame(data) #Convierto una lista en un dataframe
df_diabetes


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
filename = 'diabetes2.csv'
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



#Llamado al API de INEGI

import requests
import json

# El token se obitne de: https://www.inegi.org.mx/servicios/api_indicadores.html ----> Método Indicadores--> Parámetros
url='https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/1002000002/es/00000/false/BISE/2.0/5fb38a11-8630-38e6-d0f2-cbe3a6e61933?type=json'
#url='https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/1002000002/es/00000/false/BISE/2.0/[Aquí va el token]?type=json'
#url="https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/6200027788/es/0700/true/BISE/2.0/5fb38a11-8630-38e6-d0f2-cbe3a6e61933?type=json"
response= requests.get(url)

if response.status_code==200:
    content= json.loads(response.content)
    print(content)
    Series=content['Series'][0]['OBSERVATIONS']   
    
    #Obtención de la lista de observaciones 
    Observaciones=[]
    for obs in Series:  
        Observaciones.append(float(obs['OBS_VALUE']));
    print("Antes del promedio")
    

    #Generación del promedio de la lista de observaciones 
    sum=0.0
    for i in range(0,len(Observaciones)): 
        sum=sum+Observaciones[i];  

    resultado=sum/len(Observaciones);
    print(resultado)
   
                       


'''
5. Desde otras librerías.
Cuando lo que queremos es hacer una prueba rápida, nos pueden resultar muy útiles los datasets que traen 
«de serie» algunos de los paquetes más populares como statsmodels, scikit-learn, o seaborn. Se trata de
 conjuntos de datos de todo tipo «para hacer pruebas» que se conocen como «Toy datasets» y de los que 
 hablaremos con más detalle en el próximo post.
 Ver el archivo 9_ImportaFicherosVarios.py

'''