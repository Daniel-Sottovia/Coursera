'''
Recursão

Algoritmo recursivo:
- Se o tamanho do problema for pequeno
-- Resolva-o diretamente
- Senão
-- Reduza-o a uma instância menor do mesmo problema
-- Aplique o algoritmo (recursivamente) à instância menor
-- Volte à instância original
'''

def fatorial(n):
    if n < 1:                     # base da recursão
        return 1
    else:
        return n * fatorial(n - 1) #chamada recursiva

import pytest

@pytest.mark.parametrize('entrada, esperado', [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120)
])

def testa_fatorial(entrada, esperado):
    assert fatorial(entrada) == esperado

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

@pytest.mark.parametrize('entrada, esperado', [
    (0, 0),
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13)
])

def testa_fibonacci(entrada, esperado):
    assert fibonacci(entrada) == esperado