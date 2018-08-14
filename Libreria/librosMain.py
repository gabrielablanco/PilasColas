pila = []

def apilar(libros):
    pila.append(libros)

def desapilar():
    print("El libro " + str(pila.pop()) + " se ha retirado de la pila")

def consultar():
    print (pila)

while True:
    print("1. Agregar libro")
    print("2. Bucar ultimo libro ingresado")
    print("3. Consultar libros")
    opcion = int(input())
    if opcion == 1:
        pe = input("Nombre del libro\n")
        apilar(pe)
    elif opcion == 2:
        desapilar()
    elif opcion == 3:
        consultar()
    else:
        break