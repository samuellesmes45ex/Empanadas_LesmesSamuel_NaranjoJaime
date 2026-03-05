import json

archivo = "empanadas.json"

def cargar_empanadas():
    try:
        with open(archivo, "r") as f:
            return json.load(f)
    except:
        return []