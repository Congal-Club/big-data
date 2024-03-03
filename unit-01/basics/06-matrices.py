# Creando una matriz, que es una estructura con n listas
matriz = [[2, 4, 6], [8, 10, 12], [14, 16, 18]]

print(matriz)
print(matriz[1][2])
print(matriz[0][2])

# Agregar un elemento a la matriz
matriz.insert(3, [20, 22, 24]) # Se indica índice primero y los datos a insertar
print(matriz)

for i in range(0, 4):
    for j in range(0, 3):
        print("El valor de la posición [",i,"][",j,"]=", matriz[i][j])
