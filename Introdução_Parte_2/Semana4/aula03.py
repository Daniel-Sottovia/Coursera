"""
Seleção Direta

- A cada passo, busca pelo menor elemento do pedaço ainda não ordenado da lista e o coloca no início da lista.
- No 1° passo, busca o menor elemento de todos e o coloca na posição inicial da lista.
- No 2° passo, busca o 2° menor elemento da lista e o coloca na 2° posição da lista.
- Repete até terminar a lista.
"""
class Ordenador:
    def selecao_direta(self, lista):

        fim = len(lista)

        for i in range(fim - 1):
            # Inicialmente, o menor elemento já visto é o i-ésimo
            posicao_do_minimo = i

            for j in range(i+1, fim):
                if lista[j] < lista[posicao_do_minimo]:
                    posicao_do_minimo = j

            # Coloca o menor elemento encontrado no início da sub-lista
            # Para isso, troca de lugar os elementos nas posições i e posicao_do_minimo
            lista[i], lista[posicao_do_minimo] = lista[posicao_do_minimo], lista[i]


lista = [10, 3, 8, -10, 200, 17, 32]
o = Ordenador()
o.selecao_direta(lista)
print(lista)