def encontra_impares(lista, final=[]):
    n = len(lista)
    if n < 1:
        return final
    if lista[0] % 2 != 0:
        final.append(lista[0])
        return encontra_impares(lista[1:], final)
    else:
        return encontra_impares(lista[1:], final)


