class Bus:
    def __init__(self, placa, ruta):
        self.placa = placa
        self.ruta = ruta
        self.horarios = {}  # Diccionario con horarios asignados a conductores

    def asignar_conductor(self, conductor, horario):
        if horario in self.horarios:
            print(f"El horario {horario} ya está ocupado por otro conductor.")
        else:
            self.horarios[horario] = conductor
            print(f"Conductor {conductor.nombre} asignado al bus {self.placa} en horario {horario}.")

    def mostrar_asignaciones(self):
        if not self.horarios:
            print(f"El bus {self.placa} no tiene conductores asignados.")
        else:
            print(f"Bus {self.placa} - Ruta: {self.ruta}")
            for horario, conductor in self.horarios.items():
                print(f"  Horario: {horario} | Conductor: {conductor.nombre} ({conductor.licencia})")
