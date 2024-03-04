
'''
# Módulo Math donde viene muchas funciones matemática p
'''

# Si conoces el paquete especifico entonces 
# from math import pow
import math

x = 5
y = 4.33
z = 9.87

a =- 8

# Función para redondear un número a superior.
print("El número ", y, "redondeado a superior ", math.ceil(y))
print("El número ", y, "redondeado a inferior5 ", math.floor(y))

# Función que regresa el valor absoluto
print("El valor absolto de ",a, " es", math.fabs(a))

# Función que devuelve el factorial de
print("El factorial de ",x, " es", math.factorial(x))

# Función de potencia
print("El factorial de ",x, " elevado a la 4 es ", math.pow(x,4))

# Función de raiz cuadrada
print("El raiz cuadrada de",z, " es", math.sqrt(z))

# Función trigonométrica, coseno
print("El coseno de 90 es,", math.cos(90))

# Función trigonométrica, seno
print("El seno de 90 es,", math.sin(90))

# Función trigonométrica, tangnte
print("La tangente de 90 es, ",math.tan(90))

# Convertir de radianes a grados
print("El ángulo 90 convertido de radiames a grados es:, ",math.degrees(90))
print("El ángulo 90 convertido de grados a radianes es:, ",math.radians(90))
print("El valor de la constancia PI es :, ",math.pi)
