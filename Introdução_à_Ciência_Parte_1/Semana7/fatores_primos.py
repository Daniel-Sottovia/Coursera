n = int(input("Digite um número inteiro >1: "))

fator = 2

while n > 1:
    multiplicidade = 0
    while n % fator == 0:
        multiplicidade += 1
        n = n / fator
    if multiplicidade > 0:
        print(f"fator {fator} multiplicidade = {multiplicidade}")
    fator = fator + 1