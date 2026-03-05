def editar(empanadas):

    nombre = input("Nombre de la empanada a editar: ")

    for e in empanadas:

        if e["nombre"] == nombre:

            try:
                e["precio"] = float(input("Nuevo precio: "))
            except:
                print("Precio inválido")
                return

            e["ingredientes"] = input("Nuevos ingredientes: ")
            e["disponible"] = input("Disponible (si/no): ")

            guardar_empanadas(empanadas)

            print("Empanada actualizada")
            return

    print("Empanada no encontrada")