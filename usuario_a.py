import json

archivo = "empanadas.json"

def cargar_empanadas():
    try:
        with open(archivo, "r") as f:
            return json.load(f)
    except:
        return []

def guardar_empanadas(empanadas):
    with open(archivo, "w") as f:
        json.dump(empanadas, f, indent=4)