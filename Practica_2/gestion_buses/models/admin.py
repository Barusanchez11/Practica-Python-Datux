from models.bus import Bus
from models.conductor import Conductor

class Admin:
    def __init__(self):
        self.buses = []
        self.conductores = []

    def agregar_bus(self, placa, ruta):
        bus = Bus(placa, ruta)
        self.buses.append(bus)
        print(f" Bus agregado: {placa} - Ruta: {ruta}")

    def agregar_conductor(self, nombre, licencia):
        conductor = Conductor(nombre, licencia)
        self.conductores.append(conductor)
        print(f" Conductor agregado: {nombre} - Licencia: {licencia}")

    def asignar_conductor_a_bus(self, placa, nombre_conductor, horario):
        bus = next((b for b in self.buses if b.placa == placa), None)
        conductor = next((c for c in self.conductores if c.nombre == nombre_conductor), None)

        if bus and conductor:
            bus.asignar_conductor(conductor, horario)
        else:
            print("Bus o conductor no encontrado.")

    def mostrar_asignaciones(self):
        for bus in self.buses:
            bus.mostrar_asignaciones()
