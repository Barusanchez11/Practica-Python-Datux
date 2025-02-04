from models.admin import Admin

def menu():
    admin = Admin()

    while True:
        print("\n GESTIÓN DE BUSES Y CONDUCTORES ")
        print("1. Agregar Bus")
        print("2. Agregar Conductor")
        print("3. Asignar Conductor a Bus")
        print("4. Mostrar Asignaciones")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                placa = input("Ingrese la placa del bus: ")
                ruta = input("Ingrese la ruta del bus: ")
                admin.agregar_bus(placa, ruta)
            case "2":
                nombre = input("Ingrese el nombre del conductor: ")
                licencia = input("Ingrese la licencia del conductor: ")
                admin.agregar_conductor(nombre, licencia)
            case "3":
                placa = input("Ingrese la placa del bus: ")
                nombre_conductor = input("Ingrese el nombre del conductor: ")
                horario = input("Ingrese el horario (formato HH:MM-HH:MM): ")
                admin.asignar_conductor_a_bus(placa, nombre_conductor, horario)
            case "4":
                admin.mostrar_asignaciones()
            case "5":
                print("Saliendo del sistema...")
                break
            case _:
                print("Opción inválida, intente nuevamente.")
