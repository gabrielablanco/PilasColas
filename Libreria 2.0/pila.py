# -*- coding: utf-8 -*-
class Pila:
    """ Representa una pila con operaciones de apilar, desapilar y
        verificar si está vacía. """
 
    def __init__(self):
        """ Crea una pila vacía. """
        # La pila vacía se representa con una lista vacía
        self.items=[]

    def apilar(self, x):
        """ Agrega el elemento x a la pila. """
        # Apilar es agregar al final de la lista.
        self.items.append(x)

    def desapilar(self):
        """ Devuelve el elemento tope y lo elimina de la pila.
            Si la pila está vacía levanta una excepción. """
        try:
            return print (self.items.pop())
        except IndexError:
            raise ValueError("La pila está vacía")

    def es_vacia(self):
        """ Devuelve True si la lista está vacía, False si no. """
        return self.items == []

    def buscar(self,y,z):
        if y == 1:
            for i in range(len(self.items)):
                 if z == self.items[i][0]:
                     print(self.items[i])

        elif y == 2:
            for i in range(len(self.items)):
                 if z == self.items[i][1]:
                     print(self.items[i])

        elif y == 3:
            for i in range(len(self.items)):
                 if z == self.items[i][2]:
                     print(self.items[i])

         
                    
        
    
