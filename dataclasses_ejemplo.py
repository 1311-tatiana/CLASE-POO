from dataclasses import dataclass,field, asdict
import operaciones 
#EJEMPLO 1
"""@dataclass
class Persona: 
        nombre: str 
        edad: int = field(default=35) 

class Persona2: 
        def __init__(self, nombre, edad=35):
                self.nombre = nombre
                self.edad = edad

persona1 = Persona("Juan")
persona2 = Persona("Camila")

if persona1 == persona2:
    print("son iguales")

else:
       print("Son diferentes")"""

#EJEMPLO 2
"""@dataclass(frozen=True)
class Persona: 
        nombre: str 
        edad: int = field(default=35) 

class Persona2: 
        def __init__(self, nombre, edad=35):
                self.nombre = nombre
                self.edad = edad

persona1 = Persona("Juan", 36)
persona2 = Persona("Juan")

if persona1 == persona2:
    print("son iguales")

else:
       print("Son diferentes")"""

#EJEMPLO 3
"""@dataclass(frozen=True)
class Persona: 
        nombre: str 
        edad: int = field(default=35) 

class Persona2: 
        def __init__(self, nombre, edad=35):
                self.nombre = nombre
                self.edad = edad

persona1 = Persona("Juan", 36)
persona2 = Persona("Juan")

print(asdict(persona1))

if persona1 == persona2:
    print("son iguales")

else:
       print("Son diferentes")"""

#Ejemplo 4
@dataclass(frozen=True)
class Persona: 
        nombre: str 
        edad: int = field(default=35) 

        def retornar_edad_por_2(self) ->  int:
                return self.edad * 2
        
@dataclass
class Puesto:
        nombre: str
        persona: Persona 

persona1 = Persona("Juan", 36)
persona2 = Persona("Juan")

puesto1 = Puesto("desarrollador", persona1)

print(operaciones.suma(persona1.edad, persona2.edad))

print(puesto1)



