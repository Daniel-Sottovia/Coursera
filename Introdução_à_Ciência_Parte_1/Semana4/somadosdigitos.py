a = int(input("Digite um número inteiro: "))
b = str(a)
i = 1
soma = 0
quoeficiente = 0
while i <= len(b):
    quoeficiente = a % 10
    a = a // 10
    soma += quoeficiente
    i += 1

print(f'{soma}')
