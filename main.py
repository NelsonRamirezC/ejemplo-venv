import requests
import json


def obtener_usuarios(cantidad):
    
    url_base = f"https://randomuser.me/api/?results={cantidad}"
    
    response = requests.get(url_base)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
data = obtener_usuarios(5)

results = data.get("results")

for index, usuario in enumerate(results):
    nombre = usuario.get("name").get("first")
    apellido = usuario.get("name").get("last")
    email = usuario.get("email")
    print(index+1, nombre, apellido, email)