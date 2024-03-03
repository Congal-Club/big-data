"""
Manejo de listas, o arreglos dimensinales, bidimensiones o multidimensionales
lista, items, idices (inicia en 0)

#Declarar una lista
nombre_lista=[valor1, valor2, ...,valorN]
"""

# Creando dos listas
calif = [89, 78, 87, 88, 100]
datos = ["Javier", "Sandhez Pérez", 20, "El capulín #21", "javQgmail.com", True]

# Mostrando los valore de las listas calif y datos
print("Mostrando la lista de calificaciones: ")
print(calif)
print("Mostrando la lista datos: ")
print(datos)

# Puede manipular 
print("Mostrando información del estudiante 5 ")
print(calif[4])

# Eliminar elemento en una lista
calif[2] = []
print(calif)

# Agregar elmento en calif
calif[2] = 77
print(calif)

# Eliminar por completo una lista
# calif[:]=[]
# print("Borrando la lista!")
# print(calif)

# Una medir la dimensión de una lista
print("La lista calif contiene ", len(calif), "elementos")
print("La lista daots contiene ", len(datos), "elementos")

# Anidar listas, concatenar listas
anidada = ["Aguascalientes", "Calvillo", "Mexico", datos, calif]
print("Mostrando la lista anidada" + '\n')
print(anidada)

print("Datos de la Escuela ")
print(anidada[0:3])

print("Datos del alumnos ")
print(anidada[3])

print("Califiacaiones del alumnos ")
print(anidada[4])
