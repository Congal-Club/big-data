
"""
Created on Wed Mar  3 10:03:42 2021

@author: Elvia

Importar archivos de Excel
pandas-- es la libreria que ayuda a importar datos y convetirlos a data frame

"""

import pandas as pd
#Poner en la misma carpeta todos los archivos junto con los datasets

df1=pd.read_excel('C:\Python\DiagnosticoEstudiantes.xlsx', index_col=0) #Sin índice en columna y filas
df2=pd.read_excel('C:\Python\DiagnosticoEstudiantes.xlsx', index_col=None, header=None) #Con índices

#print(df1)

df1=pd.DataFrame(df)
print(df1.head(10))

#Sumar valor 1 con valor 2
df2=df1["Aplicar algoritmos computacionales."]+df1["Aplicar técnicas de modelado para la solución de problemas. "]*2
print(df2)

