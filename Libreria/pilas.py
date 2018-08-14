#Se crean las listas a utilizar
alfabeto = list('abcdefghijklmnopqrstuvwxyz')
digitos = list('0123456789')
n = 50
pila = []
EP = []
tope = -1

#Función de apilar información
def apilar(x, y):
    pila.append(x, y)

#Función de desapilar información
def desapilar():
    pila.pop()

#Consulta toda la pila que está llena de libros
def consultar():
    print(pila)

#Verifica si la pila se ha pasado del tope
def llena():
    if(tope == (n - 1)):
        print("La pila de libros esta llena")
        return True
    return False

#Verifica si la pila se encuentra vacia en caso de que se desee consultar la pila o el último libro
def vacia():
    if(tope == -1):
        print("La pila está vacia")
        return True
    return False

#Añade el nombre del libro a la pila y le suma un número de más al tope
def push(dato):
    if(llena()!= True):
        global tope
        tope = tope+1
        pila.apilar(tope, dato)

#Saca de la pila el último elemento que se añadió
def pop():
    if (vacia()!= True):
        global tope
        aux = pila[tope]
        del pila[tope]
        tope = tope-1
        return aux
    else:
        return -9999

def infijo(i, EI):
    if(EI[i] == '^'):
        prioridadop = 4
        return prioridadop
    elif (EI[i] == '*'):
        prioridadop = 2
        return prioridadop
    elif (EI[i] == '/'):
        prioridadop = 2
        return prioridadop
    elif (EI[i] == '+'):
        prioridadop = 1
        return prioridadop
    elif (EI[i] == '-'):
        prioridadop = 1
        return prioridadop
    elif (EI[i]=='('):
        prioridadop=5
        return prioridadop

def pripila(pila):
    if(pila[tope]=='^'):
        prioridadpi=3
        return prioridadpi
    elif(pila[tope]=='*'):
        prioridadpi=2
        return prioridadpi
    elif(pila[tope]=='/'):
        prioridadpi=2
        return prioridadpi
    elif(pila[tope]=='+'):
        prioridadpi=1
        return prioridadpi
    elif(pila[tope]=='-'):
        prioridadpi=1
        return prioridadpi
    elif(pila[tope]=='('):
        prioridadpi=5
        return prioridadpi


eistring = input("ingrese la operacion sin espacios")
EI=list(eistring.upper())
x=0
y=0
for i in range(len (EI)):
    if (EI[i] in alfabeto or EI[i] in digitos):
        EP.append(EI[i])

    elif(EI[i]!= ')'):
        if (tope==-1):
            push(EI[i])
        else:
            if (infijo(i,EI)<=pripila(pila)):
                EP.append(pop())
                push(EI[i])
            elif(infijo(i,EI)>pripila(pila)):
                push(EI[i])
    elif(EI[i]==')'):
        while (pila[tope]!='('):
            EP.append(pop())
        if (pila[tope]=='('):
            pop()
            x=x+1
        elif (tope!=-1):
            EP.append(pop())

while (tope>-1):
    EP.append(pop())
print (''.join(EP))