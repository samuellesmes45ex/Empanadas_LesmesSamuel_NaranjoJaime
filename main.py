from usuario_a import cargar_empanadas, listar, agregar
from usuario_b import editar, eliminar

def mostrar_menu():
    print("\n=== MENU EMPANADAS ===")
    print("1. Listar empanadas")
    print("2. Agregar empanada")
    print("3. Editar empanada")
    print("4. Eliminar empanada")
    print("5. Salir")

def main():

    empanadas = cargar_empanadas()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            listar(empanadas)

        elif opcion == "2":
            agregar(empanadas)

        elif opcion == "3":
            editar(empanadas)

        elif opcion == "4":
            eliminar(empanadas)

        elif opcion == "5":
            print("Programa terminado")
            print("Programa terminado")
            print("Programa terminado")
            print("Programa terminado")
            break

        else:
            print("Opción inválida")

if __name__ == "__main__":
    main()