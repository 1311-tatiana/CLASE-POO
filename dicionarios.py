"""# clave-valor 

#Creamos agenda con tres contactos 
agenda = {
    "ana": "3001112233",
    "bruno": "3154445566",
    "Carla": "3017778899"
}

#Agregar elemento o modificar
agenda["juan"] = "3001010101"
agenda["carlos"] = ["158195656", "3146982020"]

#Eliminar un elemento 
del agenda["ana"]

#mostrar todos los valores del diccionario 
print("Diccionario compleo: ", agenda)

#mostrar el numero de contacto especifico 
print("Telefono de bruno:", agenda["bruno"])

nombre = input ("ingrese el nombre de la persona: ")

if nombre in agenda:
    print("telefono de" + nombre, agenda[nombre])
else:
    telefono = input("Ingrese el telefono")
    agenda[nombre] = telefono"""

"""estudiantes = { 
    "Lucia": [4.5, 3.8, 4.2], 
    "Mateo": [3.0, 3.5, 4.0, 4.2],
    "Sofia": [5.0, 4.8, 4.9], 
     }

promedios = {}
for nombre, notas in estudiantes.items():
    prom = sum(notas) / len(notas)
    print(f"Promedio de {nombre}: {prom: .2f}")
    promedios[nombre] = prom 

print(promedios)
    
#encontrar el mejor promedio 
mejor_estudiante = max(promedios, key=promedios.get)
print(mejor_estudiante, promedios[mejor_estudiante])"""

#Inventario inicial 
inventario = { }

print("Bienvenido al programa")

while True:
    print("1. agregar productos")
    print("2. vender productos")
    print("3. Inventario")
    print("0. Salir")

    opcion = int(input())

    if opcion == 1: 
        nombre_producto = input("Ingrese nombre del producto: ")
        cantidad = int(input("Ingrese cantidad del producto: "))
        
        if nombre_producto in inventario:
            inventario[nombre_producto] += cantidad
        else:
            inventario[nombre_producto] = cantidad

        print("Inventario actualizado!")

    if opcion == 2: 
        nombre_producto = input("Ingrese nombre del producto: ")
        
        if nombre_producto in inventario:
            cantidad = int(input("Ingrese cantidad del producto: "))
            if inventario[nombre_producto] >= cantidad:
                inventario[nombre_producto] -= cantidad
                print("Inventario actualizado!")
            else: 
                print("No hay cantidad suficiente")

        else: 
            print("Producto no existe")
       
    elif opcion == 3:
        print(inventario)
    elif opcion == 0:
        print("Hasta luego")
        break 
    else: 
        print("Opcion no permitida")