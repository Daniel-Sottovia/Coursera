def maior_elemento(lista):
    a = lista[0]
    for i in lista:
        if i > a:
            a = i
    return a