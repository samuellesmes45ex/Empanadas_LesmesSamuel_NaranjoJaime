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

def listar(empanadas):

    if len(empanadas) == 0:
        print("No hay empanadas registradas")
        return

    for e in empanadas:
        print("\n------------------")
        print("Nombre:", e["nombre"])
        print("Precio:", e["precio"])
        print("Ingredientes:", e["ingredientes"])
        print("Disponible:", e["disponible"])

def agregar(empanadas):

    nombre = input("Nombre: ")

    try:
        precio = float(input("Precio: "))
    except:
        print("Precio inválido")
        return

    ingredientes = input("Ingredientes: ")
    disponible = input("Disponible (si/no): ")

    empanada = {
        "nombre": nombre,
        "precio": precio,
        "ingredientes": ingredientes,
        "disponible": disponible
    }

    empanadas.append(empanada)
    guardar_empanadas(empanadas)

    print("Empanada agregada correctamente")