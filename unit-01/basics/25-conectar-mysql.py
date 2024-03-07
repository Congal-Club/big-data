# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 13:09:16 2023

@author: elvia
"""
#Instalar los modulos necesarios

import mysql.connector # Instalar en el prompt de Anaconda el pip mysql.connector() o conda install mysql.connector
from mysql.connector import Error

try:
    mi_conexion=mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database='ControlEscolar'
        )
    
    if mi_conexion.is_connected():
        print("Conexión exitosa!!")
        infoServer=mi_conexion.get_server_info()
        print("Información del servidor:  ",infoServer)

    #Primera forma de mostrar los datos a manera de lista
    mi_cursor=mi_conexion.cursor(buffered=True)
    mi_cursor.execute("Select * FROM Carreras")
    resultados=mi_cursor.fetchall()
    # resultados=mi_cursor.fetchone()
    print(resultados)

 #Segunda forma de mostrar los dato a manera de tuplas
    for r in resultados:
       print(r)
    
    mi_cursor.close()
    mi_conexion.close()
    
except Error as ex:
    print("Ha ocurrido un error duante la conexión!  ",ex)
finally:
     if mi_conexion.is_connected():
         mi_conexion.close()
         print("La conexión ha finalizado!!")
    
    