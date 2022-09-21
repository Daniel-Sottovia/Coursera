'''
Melhoria no algoritmo da Bolha

- Percorre a lista múltiplas vezes, a cada passagem, compara todos os elementos adjacentes e troca de lugar os que estiverem fora de ordem.
- Melhoria: se em uma das iterações, nenhuma troca é realizada, isso significa que a lista já está ordenada e podemos finaliza o algoritmo.
'''

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

    def bolha(self, lista):
        fim = len(lista)

        for i in range(fim-1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]


    def bolha_curta(self, lista):
        fim = len(lista)

        for i in range(fim - 1, 0, -1):
            trocou = False
            for j in range(i):
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    trocou = True
            if trocou == False:
                return


import random
import time

class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [random.randrange(1000) for x in range(n)]
        return lista

    def lista_quase_ordenada(self, n):
        lista = [x for x in range(n)]
        lista[n//10] = -500
        return lista

    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]

        o = Ordenador()

        print('Comparando com listas aleatorias')
        antes = time.time()
        o.bolha_curta(lista1)
        depois = time.time()
        print(f'Bolha curta demorou {depois - antes}')

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print(f'Selecao direta demorou {depois - antes}')

        print('\nComparando com listas quase ordenadas')

        lista1 = self.lista_quase_ordenada(n)
        lista2 = lista1[:]

        antes = time.time()
        o.bolha_curta(lista1)
        depois = time.time()
        print(f'Bolha curta demorou {depois - antes}')

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print(f'Selecao direta demorou {depois - antes}')

c = ContaTempos()
c.compara(1000)

c.compara(5000)