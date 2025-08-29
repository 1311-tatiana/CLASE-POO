class GrupoAsignatura:
    def __init__(self, nombre, horario, profesor, codigo):
        self.nombre = nombre
        self.horario = horario
        self.profesor = profesor 
        self.estudiantes = []
        self.codigo = codigo

    def promedio(self):
        acumulador = 0
        for estudiante in self.estudiantes:
            acumulador = acumulador + estudiante.nota
        promedio = acumulador/len(self.estudiantes)
        return promedio
    
    def mostrar_estudiantes(self):
        for estudiante in self.estudiantes:
            print(estudiante.nombre)

    def Agregar_Estudiante(self, estudiante):
        self.estudiantes.append(estudiante)
        print("Agregado exitosamente")

class Estudiante:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota

class Profesor:
    def __init__(self, nombre, edad, experiencia):
        self.nombre = nombre
        self.edad = edad
        self.experienia = experiencia


profesor = Profesor("juan", 35, 5)
poo = GrupoAsignatura("Programacion orientada", "M-V 10-12", profesor, 62)
estudiante1 = Estudiante("Tatiana", 20, 2.5)
estudiante2 = Estudiante("Caro", 17, 3)
estudiante3 = Estudiante("Luis", 16, 5)

poo.Agregar_Estudiante(estudiante1)
poo.Agregar_Estudiante(estudiante2)
poo.Agregar_Estudiante(estudiante3)

