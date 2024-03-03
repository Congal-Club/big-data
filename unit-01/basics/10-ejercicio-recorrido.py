palabra = input("Nombre de la fruta: ")
palabra = palabra.upper()
longitud = len(palabra)
print("Longitud de la palbra: ", longitud)

# ultima = palabra[longitud-1]
indice = 0

while indice < len(palabra):
    letra = palabra[indice]
    # print(indice, palabra[indice])

    if(letra == 'A'):
        indice += 1
        continue    
    if(letra == 'E'):
        indice += 1
        continue
    if (letra == 'I'):
        indice += 1
        continue
    if (letra == 'O'):
        indice += 1
        continue
    if (letra == 'U'):
        indice += 1
        continue
    else:
        print(letra)
        indice +=  1
