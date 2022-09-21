n = int(input("Digite um número inteiro: "))

i = 2
primo = True
mult = 0
while i <= n:
    if n % i == 0:
        mult += 1
    i += 1

if mult <= 1:
    print("primo")
else:
    print("não primo")


