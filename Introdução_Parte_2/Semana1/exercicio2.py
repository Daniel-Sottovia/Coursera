def tamanho(matriz):
    return [len(matriz), len(matriz[0])]

def soma_matrizes(m1,m2):
    tam_matriz_1 = tamanho(m1)
    tam_matriz_2 = tamanho(m2)

    if tam_matriz_1 == tam_matriz_2:
        final = []

        linha = tam_matriz_1[0]
        cont_l = 0

        while cont_l < linha:
            final.append([])
            coluna = tam_matriz_1[1]
            cont_c = 0
            while cont_c < coluna:
                soma = m1[cont_l][cont_c] + m2[cont_l][cont_c]
                final[cont_l].append(soma)

                cont_c += 1

            cont_l += 1

        return final

    else:
        return False

