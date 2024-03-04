"""

Conjunto de subrutinas o subprogrmas que pueden ser ejecutas 
 desde un programa o desde otro programa

Sirve para reutilizar código
Este módulo se manda llamar de otro archivo llamado principal.py

"""

def positivos():
    print("Funcion positivos")
    for i in range(10,50,10):
        print(i)
        print("Vas bien---")
    

def negativos():
    print("Funcion negativos")
    for i in range(-10,-50,-10):
        print(i)

def pares():
    print("Función pares")
    for i in range(2,10,2):
        print(i)
    
    
def impares():
    print("Función impares")
    for i in range(1,10,2):
        print(i)
