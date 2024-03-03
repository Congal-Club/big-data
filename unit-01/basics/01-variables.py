# En este programa se analiza como definir variables.

# Como saber que tipo de variable, solo se pasa el argumento y Python lo sabe

edad = 22 # Estoy creando una var tipo int
nombre = "Cesar Villalobos Olmos" # Variable tipo String
promedio = 98.4 # Variable tipo flotante
email = "20151608@aguscalientes.tecnm.mx" #Var tipo String
EstCivil = False  # Variable tipo Booleana.

print(f"Su nombre es: {nombre}")
print("Su edad es: ", edad)
print ("Su promedio es: ", promedio)
print("Su correo es ", email)
print("Su estado civil es: ", EstCivil," años.")

if EstCivil == True:
    print("Usted es casado.")
else:
    print("Usted es soltero.")
