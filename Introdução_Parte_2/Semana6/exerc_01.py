def soma_lista(lista):
    n = len(lista)
    if n == 1:
        return lista[0]
    else:
        return lista[0] + soma_lista(lista[1:])

