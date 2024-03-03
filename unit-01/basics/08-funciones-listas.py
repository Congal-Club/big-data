# Definiendo la estructura de una lista
lista = ["José", 33, 56.7, True, "jos@gmail.com"]
print(lista)

# Función append
# Agregara una elmmento al final de la lista
lista.append("Casado")
print(lista)

# Agregar más de un elemnto a una lista
lista.extend([56,"Jardin"])
print(lista)

# Agregar un elemento en la posición que se indique y recorre los valores de la lista
lista.insert(0,"Juan")
print(lista)

# Elimina un elemento que se desea 
lista.remove(True)
print(lista)

# Cuenta el número de elementos que tiene una lista
print("Valores repetidos ",lista.count("José"))

# Ordenar número de una lista (sort)

numeros = [2, 5, 37, 6, 78, 87, 67]
print("Números originales: ", numeros)
print("Números ordenados: ")
numeros.sort()
print(numeros)

# Ordena de manera descendentes
numeros.reverse()
print("Números ordenados descendente")
print(numeros)

# Eliminar un elemento de la lista en el índice indicado
numeros.remove(2)
numeros.remove(87)
print(numeros)

del numeros[2]
print(numeros)

# Extraer un elemento de la lista, eliminando el último
numeros.pop()
print(numeros)

# Extraer un elemento de la lista, pero un valor especifico de elementos
numeros.pop(2)
print(numeros)
