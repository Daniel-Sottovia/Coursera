def imprime_matriz(matriz):
    linha = len(matriz)
    cont_l = 0
    while cont_l < linha:
        coluna = len(matriz[cont_l])
        cont_c = 0
        while cont_c < coluna:
            if cont_c == coluna - 1:
                print(f'{matriz[cont_l][cont_c]}', end='\n')
            else:
                print(f'{matriz[cont_l][cont_c]}', end=' ')
            cont_c += 1
        cont_l += 1
