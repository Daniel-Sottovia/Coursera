import random

def lista_grande(n):
    lista = []
    cont = 0
    while cont < n:
        lista.append(random.randrange(n))
        cont += 1
    return lista


