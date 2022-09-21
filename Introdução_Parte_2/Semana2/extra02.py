def primeiro_lex(lista):
    tam = len(lista)
    cont = 0
    valor_menor = 0
    palavra = ''
    while cont < tam:
        if cont == 0:
            valor_menor = ord(lista[cont][0])
            palavra = lista[cont]
        elif valor_menor > ord(lista[cont][0]):
            valor_menor = ord(lista[cont][0])
            palavra = lista[cont]
        cont += 1
    return palavra
