from cola import *
q = Cola()

while True:
    print("1. Agregar usuarios")
    print("2. Desencolar usuarios")
    opcion = int(input())
    
    if opcion == 1:
        x = int(input("Cuantos usuarios desea ingresar en el parqueadero"))
        for i in range(x):
            print("Ingrese el nombre del estudiante: ")
            nom = input()
            print("Ingrese el codigo del estudiante")
            cod = input()
            print("Ingrese la placa del vehiculo")
            plac = input()
            items = [nom, cod, plac]
            q.encolar(items)
    elif opcion == 2:
        q.desencolar()
    else:
        break

print("Los datos han sido añadidos correctamente")


