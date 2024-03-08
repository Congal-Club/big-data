# Graficar los datos 

import matplotlib.pyplot as plt
import numpy as np

año=[1990,2000,2010,2020] # Población
pob=[5.5,6,7,7.8,] # Año

#Diagram de líneas
plt.plot(año,pob)
#plt.show()
#plt.draw()

# Generar un Diagrama de dispersión de puntos
fig,ax=plt.subplots()
plt.ylabel('Ejem y')
plt.xlabel('Ejem x')
ax.scatter(x=[1,2,3], y=[3,2,1])

# plt.show()

#Diagrama de áreas
fig,ax=plt.subplots()
ax.fill_between([1,2,3,4],[1,2,0,0.5])
#plt.show()

#Graficar Histogramas
fig,ax=plt.subplots()
x=np.random.normal(5,1.5,size=1000)
ax.hist(x,np.arange(0,11))
#plt.show()


#Diagrama de sectores
fig,ax=plt.subplots()
ax.pie([5,4,3,2,1])
#plt.show()

#Graficando diversos datos con colores distintos
fig,ax=plt.subplots()
dias=['L','M','X','J','V','S','D']
temperaturas={'Aguascalientes':[28.5,30.5,31,30,28,27.5,30.5],'Calvillo':[24.5,25.5,26.5,25,26.5,24.5,25]}
ax.plot(dias,temperaturas['Aguascalientes'],color='tab:purple',label='Aguascalientes')
ax.plot(dias,temperaturas['Calvillo'],color='tab:green',label='Calvillo')
ax.legend(loc='lower right')
plt.show()
#plt.draw()

