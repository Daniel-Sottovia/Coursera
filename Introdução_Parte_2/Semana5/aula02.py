'''
Comparação de Desempenho

-Módulo time
-- Função time()
-- Devolve o tempo decorrido (em segundos) desde 1/1/1970 (no Unix)
'''
import random
import time

from aula01 import Ordenador

class ContaTempos:
    def lista_aleatoria(self, n):
        lista = [random.randrange(1000) for x in range(n)]
        for i in range(n):
            lista[i] = random.randrange(1000) # inteiros entre 0 e 999
        return lista

    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]

        o = Ordenador()

        antes = time.time()
        o.bolha(lista1)
        depois = time.time()
        print(f'Bolha demorou {depois - antes}')

        antes = time.time()
        o.selecao_direta(lista2)
        depois = time.time()
        print(f'Selecao direta demorou {depois - antes}')

c = ContaTempos()
c.compara(5000)


