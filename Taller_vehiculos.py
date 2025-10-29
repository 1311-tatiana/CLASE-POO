class Empresa:
    def __init__(self, nombre, vehiculo):
        self.nombre = nombre 
        self.vehiculo = vehiculo 
    
    def mostrar_informacion(self):
        pass 

    def resumen_flota(self):
        pass

    def guargar_en_archivo(self):
        pass

    
class Vehiculo(Empresa):
    def __init__(self, placa, modelo, marca):
        self.placa = placa 
        self.modelo = modelo 
        self.marca = marca 

class Moto(Vehiculo):
    pass
class Camion(Vehiculo):
    pass

class Autoparticular(Vehiculo):
    pass 
