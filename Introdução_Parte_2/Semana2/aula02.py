x, y = 10, 20

a, b, c = 1, 2, 3

def peso_altura():
    return 77, 1.83

peso , altura = peso_altura()
print(peso)
print(altura)

a = 10
b = 20
a, b = b, a

'Atribuição Aumentada'
x = 10
x = x + 10
x += 10
x *= 2
x **= 2

def pagamento_semanal(valor_por_hora, num_horas = 40):
    assert valor_por_hora >=0 and num_horas > 0
    return valor_por_hora * num_horas

paga = pagamento_semanal(100, 36)
print(paga)

x = 10
x += 10
x /= 2
x //= 3
x %= 2
x *= 9
print(x)