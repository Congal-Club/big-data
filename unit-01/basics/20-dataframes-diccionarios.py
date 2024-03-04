
import pandas as pd

'''
  Crear un dicionario con países y sus capitales.
'''

info_pais={"pais":["Brasil","México","España","Perú","Colombia","Venezuela"],"Capital":["Brasilia","Cdmx","Madrid","Lima","Bogotá","Caracas"],"Superficie (Mkm2)":[8.5,1.9,1.2,0.5,1.1,0.9]}
#Construir un dataframe desde un diccionario
df_pais=pd.DataFrame(info_pais)
print(df_pais)
