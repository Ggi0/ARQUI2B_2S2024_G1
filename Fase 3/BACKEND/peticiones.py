import requests
import json

respuesta = requests.get("https://vercel-bd.vercel.app/api/colecciones/")
try:
    data = respuesta.json()
    print(data)
except json.JSONDecodeError:
    print("La respuesta no es un JSON válido:")
    print(respuesta.text)