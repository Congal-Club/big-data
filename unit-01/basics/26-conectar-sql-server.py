# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 13:55:20 2023

@author: User
"""

#Importar las librrias que vamos requerir
import pyodbc #Instalar el prompt de Anaconda el pip pyodbc() conda install pyodbc
import pandas as pd  # Contiene funciones que nos ayudan en el manejo de nuestros datos.

server='XPS-ERB\SQLEXPRESS'
db='ControlEscolar'
#username = 'sa' 
#password = 'sss'

#REALIZAR LA CONEXIÓN
conexion=pyodbc.connect(driver='{SQL Server}',server=server,database=db)

print(conexion)
print("Conexióne exitosa")

#REALIZAR LAS CONSULTAS DESEADAS
valores=pd.read_sql('SELECT * FROM Carreras',conexion)
#valores=pd.read_sql('SELECT Alumnos.NoC,NombreA, Carreras.NombreC FROM Carreras, Alumnos WHERE Carreras.NoC=Alumnos.NoC and Alumnos.NoC=1',conexion)
print(valores)


#SIEMPRE DEBEMOS CERRAR LAS CONEXIONES
conexion.close()


#OTRA MANERA DE CONECTAR
'''
#conexion=pyodbc.connect(driver='{ODBC Driver 18 for SQL Server}',host=server,DATABASE=database,UID=username,PWD=password)
#conexion=pyodbc.connect(driver='{ODBC Driver 18 for SQL Server}',host=server,DATABASE=database,UID=username,PWD=password)
#conexion=conexion.cursor()
print("Conexióne exitosa")

#Sample select query
cursor.execute("SELECT @@version;") 
row = cursor.fetchone() 
while row: 
    print(row[0])
    row = cursor.fetchone()
 '''


