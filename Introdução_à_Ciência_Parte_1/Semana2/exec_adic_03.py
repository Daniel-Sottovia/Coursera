numero = int(input("Digite um número inteiro: "))

unidade = numero % 10
resto = (numero-unidade) / 10
dezena = int(resto % 10)

print(unidade)

print(f"O dígito das dezenas é {dezena}")