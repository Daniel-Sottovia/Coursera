def maximo(x, y, z):
    lista = [x, y, z]
    b = lista[0]
    for i in range(3):
        if lista[i] > b:
            b = lista[i]
    return b
