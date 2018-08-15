from pila import *
p = Pila()

while True:
    print("1. Agregar libro")
    print("2. Buscar libro")

    opcion = int(input())
    if opcion == 1:
        print("Ingrese el título del libro: ")
        titulo = input()
        print("Ingrese el autor del libro: ")
        autor = input()
        print("Ingrese el genero del libro: ")
        genero = input()
        libro = [titulo, autor, genero]
        p.apilar(libro)
    elif opcion == 2:
        print("1. Buscar por Título")
        print("2. Buscar por Autor")
        print("3. Buscar por Género")
        opcion2 = int(input())
        bus = input("Buscar: ")
        p.buscar(opcion2,bus)

    else:
        
        break
