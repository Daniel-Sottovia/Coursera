def primo():
    n = int(input("Digite um número inteiro positivo: "))
    i = 2
    cont = 0
    while i <= n:
        if n % i == 0:
            cont += 1
        i += 1
    if cont <= 1:
        return True
    else:
        return False

print(primo())