# Creación y manipulación de listas- inicia el valor desde la posción 0
dimensiones = [14, 18, 22, 13, 27, "mesa"]
print(dimensiones)
print(dimensiones[4])
print(dimensiones[-2])
print(dimensiones[1:5]) # imprime hasta la posición 5-1
print(dimensiones[1:-1])

# Creación de listas
# for
numeros = [3,6,7,2,8]
numeros_sum_5 = []
for num in numeros:
    numeros_sum_5.append(num + 5)

print(numeros_sum_5)

# Comprensión de listas
numeros_sum_5_c1 = [num + 5 for num in numeros]
print(numeros_sum_5_c1)

# Creación de una lista que eleve al cuadrado los valores pares de la lista.
# par nume % 2 ==0

numeros_cuadrado = [num ** 2 if num % 2 == 0 else num for num in numeros]
print(numeros)
print(numeros_cuadrado)
