# Estructuras de control de flujo de datos

# IF-----IF -----------------------
print("Ingresa tu edad: ")
edad = int(input())

if (edad<=18):
    print("Eres mayor de edad--")
else:
    print("Eres menor de edad---")
    

print("Dar un valor de importe")
importe = int(input())

if (importe>100):
    desc = 10
    imp_desc = importe * desc / 100
    pagar = importe - imp_desc

    print("El valor a pagar es: ", pagar)
else:
    pagar = importe
    print("El valor a pagar es: ", pagar)
    
    
print("Dar el valor de 1 a 3")
n = int(input())

if n == 1:
    print("AGUASCALIENTES ")
elif n==2:
    print("BAJA CALIFORNIA")
elif n == 3:
    print("BAJA CALIFORNIA SUR")
else:
    print("Inválido")

# WHILE-----WHILE
numero = 1
while numero <= 10:
    print (numero)
    numero += 1

# FOR-----FOR
for numero in range(1, 11):
    print (numero)

#D O-WHILE---DO WHILE
Continua = "s"
Numero = 1
while continua == "s":
    print(numero)
    numero += 1
    print("Continuar s/n")
    nombre = input()
