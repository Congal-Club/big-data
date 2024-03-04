# Listas
alumnos = ["Raúl","María","Rubén","Verónica","Diego","Esteban"]
notas_alumnos = [9,7.5,8,9.5,6,7]
print(alumnos)
print(notas_alumnos)

ind_rub = alumnos.index("Rubén")
print(notas_alumnos[ind_rub])

# Hacer lo anterior pero con diccionario
alumnos_dic = {"Raul":9,"María":7.5,"Rubén":8,"Verónica":9.5,"Diego":6,"Esteban":7}
print(alumnos_dic)
print(alumnos_dic["Rubén"])

# Como construir un diccionario a partir de listas
# Se pude usar la función zip(concatenacion de datos en formato json) 
# para crear diccionarios con base a listas.

pais = ["España","México","Venezuela","Colombia","Perú","Argentina"]
poblacion = [47,128,32,50,33,45]
sueldo = [12000,15000,2000,3000,4000,50000]

dic_pais = dict(zip(pais,poblacion))
print(dic_pais["México"])
