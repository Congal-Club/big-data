cadena = "Hola cómo estás"

# Devuelve la cadena con e primer caracter en mayúscula.
print(cadena.capitalize())

# Centra la cadena de texto con los espacios indicados
print(cadena.center(30))

# Devolver como resultado el tamaño de una cadena
print(len(cadena))

# Devuelve el número de veces que se encuentra una cadena en otra
print(cadena.count("o",0,15))
print(cadena.count("o",0,len(cadena)))

# Devolver verdadero si todos los caracters son albanuméricos
print(cadena.isalnum())

# Devolver True si todos los caracteres son numéricos
cadena2="1234a"
print(cadena2.isdigit())

# Devuelve tru si todos los caracteres están en minúsculas.
print(cadena2.islower())

# Devuelve si todos los caracteres están en mayúscula.
print(cadena.isupper())

# Convierte una cadena a minúsculas
print(cadena.lower())

# Convierte una cadena a mayúscula
print(cadena.upper())

# Remplaza una cadena por otra
print(cadena.replace( "cómo estás"," cómo,¿Estás?"))

# La cadena es una arreglo
print(cadena[3])
print(cadena[2:15])
