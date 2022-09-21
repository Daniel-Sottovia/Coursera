def busca(lista, elemento):
    tam = len(lista)
    cont = 0
    while cont < tam:
        if lista[cont] == elemento:
            return cont
        cont += 1

    return False
