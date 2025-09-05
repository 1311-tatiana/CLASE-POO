class Persona:
    def __init__(self, nombre, cedula, ti):
        self.nombre = nombre
        self.__cedula = cedula
        self.__ti = ti
    
    def obtener_documento(self):
        if self.__cedula is not None:
            return self.__cedula
        else:
            return self.__ti

persona1 = Persona("juan", 11111, None)
persona2 = Persona("Maria", 22222, None)
niño1 = Persona("Isaac", None, 3333)

print("el nombre de la primera persona es", persona1.nombre)
"""print("la cedula de la primera persona es", persona1.__cedula)""" # con doble guion bajo ponemos los atributos privados 
print("el documento de la primera persona es", persona1.obtener_documento())

print("el nombre de la segunda persona es", persona2.nombre)
print("el documento del primer niño es", niño1.obtener_documento())
