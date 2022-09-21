"""
Quebrar o problema em problemas menores
Testes automatizados
Refatoração
Eliminar código duplicado
"""
def MinMax(temperaturas):
    print(f"A menor temperatura do mês foi: {minima(temperaturas)} C.")
    print(f"A maior temperatura do mês foi: {maxima(temperaturas)} C.")

def maxima(temps):
    max = temps[0]
    i = 0
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i = i + 1
    return max

def minima(temps):
    min = temps[0]
    i = 0
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i = i + 1
    return min

def teste_pontual(temp, valor_esperado):
    valor_calculado = minima(temp)
    if valor_calculado != valor_esperado:
        print(f"Valor errado para array {temp}")
        print(f"Valor esperado: {valor_esperado}. Valor calculado: {valor_calculado}")


def testa_minima():
    print("Iniciando os testes")
    teste_pontual([0], 0)
    teste_pontual([0, 0, 0, 0, 0, 0], 0)
    teste_pontual([0, 1, 2, 3, 4, 5, 8, 9, 10], 0)
    teste_pontual([30, 27, 26, 26, 29, 31, 32, 33, 30], 26)
    teste_pontual([-15, -12, 0, 20, 30], -15)
    print("Finalizando os testes")

MinMax([30, 27, 26, 26, 29, 31, 32, 33, 30])