class Dispositivo: 
    def __init__(self, nombre):
        self.nombre = nombre 
        self.estado = False

    def encender(self):
        self.encender = True 
        print(self.nombre, "encendido")

    def apagar(self):
        self.estado = False
        print(self.nombre, "apagado")

class Espacio:
    def __init__(self, nombre):
        self.nombre = nombre 
        self.__dispositivos = []

    def agregador(self, dispositivo):
        self.__dispositivos.append(dispositivo)

    def mostrar(self):
        for dispositivo in self.__dispositivos:
            print(dispositivo.nombre)

class Casa: 
    def __init__(self, direccion):
        self.direcion = direccion 
        self.__espacios = []

    def agregador(self, nombre):
        self.__espacios.append(Espacio(nombre))
        print("Espacio agregado")

    def buscare(self, nombre):
        for espacio in self.__espacios:
            if espacio.nombre == nombre:
                return espacio
        return None 

    def mostrare(self):
        for espacio in self.__espacios:
            print(espacio.nombre)

mi_casa = Casa("Calle 123")
mi_casa.agregador("cocina")
mi_casa.agregador("Habitacion")
mi_casa.agregador("Baño")
television = Dispositivo("Television")
mi_casa.buscare("Habitacion").agregador(television)
mi_casa.buscare("Habitacion").mostrar()

