from cola import *
q = Cola()

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

print("Los datos han sido añadidos correctamente")

