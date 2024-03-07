# Para escribir solo una línea de código.

"""
Escribir bloques de texto.
"""

'''
 Se puede usar el paquete pandas para importar datos desde archivos en formato
 CSV.
'''

import pandas as pd

#df
df = pd.read_csv(r'Info_pais.csv', encoding="ISO 8859-1", delimiter=";")
print(df.info)
print(df)
print(df.head(10)) # Imprimir los diez primeros datos.

# Ordenar los datos de manera ascendente por la columna de esperanza de vida.

# df_order=df.sort_values("Esperanza de vida", ascending=True)
df_order=df.sort_values("Esperanza de vida", ascending=False)
print(df_order.head(10))

# Crear un data frame nuevo para manipular los datos de la tabla original.
# Dato_a_modificar=pd.DataFrame(df["Esperanza de vida"])
df.Poblacion
dato2 = pd.DataFrame(df.get("País"))
datos_pais = pd.DataFrame(df.get("Poblacion"))
dato3 = df["País"]
Dato_a_modificar = df[["País","Esperanza de vida","Poblacion"]]

# Filtrar por filas
