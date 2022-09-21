'''
Algoritmo da Busca Binária

- Objetivo: localizar elemento x em uma lista
- Considere o elemento m do meio da lista
-- x == m => encontrou!
-- x < m => procure apenas na 1° metade (esquerda)
-- x > m => procure apenas na 2° metade (direita)
- Repita o processo até que o x seja encontrado ou que a sub-lista em questão esteja vazia.

- Dado uma lista de n elementos
- No pior caso, teremos que efetuar
-- log n na base 2 comparações

- Ao estudar a eficiência de um algoritmo é interessante:
-- Analisar a complexidade computacional
-- Realizar experimentos medindo o desempenho
'''

class Buscador():
    def busca_sequencial(self, lista, x):
        for i in range(len(lista)):
            if lista[i] == x:
                return i
        return -1

    def busca_binaria(self, lista, x):
        primeiro = 0
        ultimo = len(lista) - 1

        while primeiro <= ultimo:
            meio = (primeiro + ultimo)//2
            if lista[meio] == x:
                return meio
            else:
                if x < lista[meio]:
                    ultimo = meio - 1
                else:
                    primeiro = meio + 1
        return -1

lista = [-100, 0, 20, 30, 50, 100, 3000, 5000]
b = Buscador()
print(b.busca_binaria(lista, 100))
print(b.busca_binaria(lista, 0))
print(b.busca_binaria(lista, -100))
print(b.busca_binaria(lista, 5000))
print(len(lista))
print(b.busca_binaria(lista, 7000))
print(b.busca_binaria(lista, 70))