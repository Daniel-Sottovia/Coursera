def ordena(lista):
    tam = len(lista)
    cont = 0
    while cont < tam:

        i = cont
        menor = cont
        while i < tam:
            if lista[i] < lista[menor]:
                menor = i
            i += 1
        lista[cont], lista[menor] = lista[menor], lista[cont]
        cont += 1
    return lista


