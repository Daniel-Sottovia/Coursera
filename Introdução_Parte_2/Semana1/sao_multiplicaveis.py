def sao_multiplicaveis(m1,m2):
    tam1 = len(m1)
    tam2 = len(m2)
    cont = 0
    while cont < tam1:
        coluna = len(m1[cont])
        if coluna != tam2:
            return False
        cont += 1
    return True
