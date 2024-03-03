"""
LLAMADA PROGRAMACIÓN MODULAR

Una funcióne es un conjunto de líneas de código que realizan una tarea
especifíca

Modularizar da como ventaja reducir líneas de código cuando se desea
realizar una tarea muy concreta.
Ventajas:
***Reutilización de código.
***Divide y venderas. Lo divides en funciones se hace fácil programarlo.
1_Practica_Python.py
Sintaxis para crear una función(se usa la palabra reservada def)

def nombre_funcion (parámetros):
    Acción1
    Acción2
    AcciónN

Sintaxis para llamar una función

nombre_funcion(parámetros)
"""

def imprime_10():
    for i in range(0,10):
        print("i  ",i,"Mensaje", i)

# Mandando llamar a la función
imprime_10()
# imprime_10()
# imprime_10()
