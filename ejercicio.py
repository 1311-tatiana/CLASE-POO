class Persona:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera 

    def repira(self):
        print(f"{self.nombre} esta repirando {self.carrera}")

class Estudiante(Persona):
    def __init__(self, nombre, notas):
        super().__init__(nombre)
        self.notas = notas 

    def estudiar(self):
        print(f"{self.nombre} esta estudianso {self.carrera}")

persona1 = Persona("carlos", "inge. sistemas")
persona1.estudiar()

persona2 = Estudiante("Cami", "derecho")
persona2.estudiar