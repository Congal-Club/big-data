# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 10:04:57 2023

@author: elvia
"""

from scipy.stats import entropy
from math import log


#Medida de la entropía en el lanzamiento de un dato Justo
print("Dado Justo: ", entropy([1/6,1/6,1/6,1/6,1/6,1/6],base=2))
print("Dado Justo: ", -((1/6)*log(1/6,2)+(1/6)*log(1/6,2)+(1/6)*log(1/6,2)+(1/6)*log(1/6,2)+(1/6)*log(1/6,2)+(1/6)*log(1/6,2)))

#Medida de la entropía en el lanzamiento de un dato Injusto
print("Dado Injusto: ", entropy([1/3,1/3,1/12,1/12,1/12,1/12],base=2))
print("Dado Injusto: ", -((1/3)*log(1/3,2)+(1/3)*log(1/3,2)+(1/12)*log(1/12,2)+(1/12)*log(1/12,2)+(1/12)*log(1/12,2)+(1/12)*log(1/12,2)))



#Medida de la entroía en lanzamiento de una moneda

