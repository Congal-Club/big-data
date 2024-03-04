def saludar(nombre):
    print("Hola como estás! ", nombre)

def bienvenida(nombre):
    print("Hola ", nombre, " Bienvenido a la Fiesta!")

def despedir(nombre):
    print("Adiós, ",nombre)
    
print("Ingrese su nombre: ")
nombre = input()

saludar(nombre)
bienvenida(nombre)
despedir(nombre)
