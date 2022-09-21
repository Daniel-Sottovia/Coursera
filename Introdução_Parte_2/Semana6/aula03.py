'''
Ordenação por Intercalação - MergeSort

- Divida a lista na metade recursivamente, até que cada sublista contenha apenas 1 elemento (portanto, já ordenada)
- Repetidamente, intercale as sublistas par produzir novas listas ordenadas.

'''

def merge_sort(lista):
    if len(lista) <= 1: #BASE DA RECURSAO
        return lista

    meio = len(lista) // 2

    lado_esquerdo = merge_sort(lista[:meio])
    lado_direito = merge_sort(lista[meio:])

    return merge(lado_esquerdo, lado_direito)

def merge(lado_esquerdo, lado_direito):
    if not lado_esquerdo:
        return lado_direito

    if not lado_direito:
        return lado_esquerdo

    if lado_esquerdo[0] < lado_direito[0]:
        return [lado_esquerdo[0]] + merge(lado_esquerdo[1:], lado_direito)

    return [lado_direito[0]] + merge(lado_esquerdo, lado_direito[1:])


a = [8, 3, 4, 1, 5, 2, 7, 0]
merge_sort(a)