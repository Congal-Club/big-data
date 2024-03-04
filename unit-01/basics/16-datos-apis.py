import requests
import json

#Llamado al API de INEGI
# El token se obitne de: https://www.inegi.org.mx/servicios/api_indicadores.html ----> Método Indicadores--> Parámetros
#url='https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/1002000002/es/00000/false/BISE/2.0/5fb38a11-8630-38e6-d0f2-cbe3a6e61933?type=json'
#url='https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/1002000002/es/00000/false/BISE/2.0/[Aquí va el token]?type=json'
url="https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/6200027788/es/0700/true/BISE/2.0/5fb38a11-8630-38e6-d0f2-cbe3a6e61933?type=json"

response= requests.get(url)

if response.status_code==200:
    content= json.loads(response.content)
    print(content)
    Series=content['Series'][0]['OBSERVATIONS']   
    
    #Obtención de la lista de observaciones 
    Observaciones=[]
    for obs in Series:  
        Observaciones.append(float(obs['OBS_VALUE']));
    print("Antes del promedio")
    

    #Generación del promedio de la lista de observaciones 
    sum=0.0
    for i in range(0,len(Observaciones)): 
        sum=sum+Observaciones[i];  

    resultado=sum/len(Observaciones);
    print(resultado)