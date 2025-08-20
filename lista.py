#Crear listas 
mi_lista = ["Primero", "segundo", "Tercero"]
print(mi_lista[1:])

# Crear listas con ceros 
listas_ceros = [0] * 10
print(listas_ceros)

import random
lista_random = [random.randint(1,100)] * 10
print(lista_random)

#crear lista con numero aleatorios
lista_random2 = [random.randint(1,100) for _ in range(10)]
print(lista_random2)

#crear lista con un rango de numeros 
lista_ejemplo = [i for i in range(0,10)]
print(lista_ejemplo)
 
#cambiar un elemento de la lista por otro
lista_ejemplo[2] = 1
lista_ejemplo [5] = 2

print(lista_ejemplo)

#elimina un elemento
lista_ejemplo.remove(1)
print(lista_ejemplo)

#elimina por posición 
del lista_ejemplo[2]
print(lista_ejemplo)

lista_ejemplo = [elemento for elemento in lista_ejemplo if elemento != 1]
print(lista_ejemplo)

#intercambiar posiciones
lista_ejemplo.reverse()
print(lista_ejemplo)

#ordenar de menor a mayor
lista_ejemplo.sort()
print(lista_ejemplo)

#ordenar mayor a menor
lista_ejemplo.sort(reverse=True)
print(lista_ejemplo)

class persona:
    def __init__(self, nombre):
        self.nombre = nombre
        self.numeros = [random.randint(100,999) for _ in range(5)]

persona1 = persona("tati")
persona2 = persona("caro")

print("los numeros para ", persona1.nombre, "son ", persona1.numeros)
print("los numeros para ", persona2.nombre, "son ", persona2.numeros)  