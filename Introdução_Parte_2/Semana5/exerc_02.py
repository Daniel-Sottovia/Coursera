def bubble_sort(lista):
    tam = len(lista) - 1
    i = 0
    while tam >= 0:
        i = 0
        while i < tam:
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                print(lista)
            i += 1
        tam = tam - 1
    return lista

