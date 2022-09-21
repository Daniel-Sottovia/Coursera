def ordenada(lista):
    tam = len(lista)
    cont = 1
    while cont < tam:
        if not lista[cont - 1] < lista[cont]:
            return False
        cont += 1
    return True