import os
os.chdir("C:\\Python")
os.getcwd()

#REVISAR ESTE BLOQUE DE CÓDIGO
import numpy
filename = 'diabetes2.csv'
raw_data = open(filename)
data = numpy.loadtxt(raw_data, delimiter=",",skiprows=1)
print(data.shape)
print(data)

import pandas as pd
df_diabetes=pd.DataFrame(data)
df_diabetes


