import requests # la librería requests nos permite hacer peticiones HTTP
import json


# Función para leer un archivo JSON
def obtener_datos_api(url="", params={}):
    url = "{}/{}/{}".format(url, params["coin"], params["method"])
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print(error)
        return {}
    
parametros = {"coin": "BTC", "method":"ticker"}
url = "https://www.mercadobitcoin.net/api"
datos = obtener_datos_api(url=url, params=parametros)

if len(datos)>0:
    print(json.dumps(datos, indent=4))
else:
    print("no se obtuvo la consulta")
