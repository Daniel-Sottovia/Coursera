def insertion_sort(lista):
    tam = len(lista)
    i = 0
    while i < tam:
        menor = i
        j = i + 1
        while j < tam:
            if lista[menor] > lista[j]:
                menor = j
            j += 1

        lista[menor], lista[i] = lista[i], lista[menor]
        i += 1

    return lista
