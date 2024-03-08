

import pandas as pd
import matplotlib.pyplot as plt


df=pd.read_csv(r'C:\Python\Info_pais.csv',encoding="ISO 8859-1",delimiter=";")
print(df)
plt.plot(df["Esperanza de vida"])
plt.show()
#plt.draw()