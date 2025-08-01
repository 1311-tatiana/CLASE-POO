class Perro:
    def __init__(self, nombre, raza):
        self.nombre = nombre 
        self.raza = raza

    def ladrar(self):
        print("El perro que esta ladrando es: ", self.nombre)


class Persona:
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre 
        self.edad = edad
        self.sexo = sexo
    
# Vamos a instanciar un objeto desde la clase Perro
print("Mi primer perrito")
mi_perrito = Perro("Mia", "Golden")
print(mi_perrito.nombre)
print(mi_perrito.raza)

print("Mi segundo perrote")
mi_perrote = Perro("Carlitos", "Salchicha")
print(mi_perrote.nombre)
print(mi_perrote.raza)

print("ingrese los datos del tercer perro")
nombre = input("Ingrese el nombre: ")
raza = input("Ingrese la raza: ")

el_tercer_perro = Perro(nombre, raza)
print("El tercer perro")
print(el_tercer_perro.nombre)
print(el_tercer_perro.raza)

print("Ahora los perros van a ladrar")
mi_perrito.ladrar()
mi_perrote.ladrar()
el_tercer_perro.ladrar()