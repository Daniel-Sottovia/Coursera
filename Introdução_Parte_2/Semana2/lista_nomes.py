def menor_nome(lista_de_nomes):
    tam = len(lista_de_nomes)
    lista = []
    cont = 0
    while cont < tam:
        lista.append(lista_de_nomes[cont].strip().capitalize())
        cont += 1
    menor = ''
    comp = 0
    cont = 0
    while cont < tam:
        if cont == 0:
            menor = lista[cont]
            comp = len(lista[cont])
        elif len(lista[cont]) < comp:
            menor = lista[cont]
            comp = len(lista[cont])
        cont += 1
    return menor
