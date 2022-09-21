numero = int(input("Digite um número inteiro: "))

b = str(numero)
resto = numero // 10
a = numero % 10
c = 0
i = 0
adjacente = True
while i < len(b) and adjacente and len(b) > 1:
    c = resto % 10
    if c == a:
        adjacente = False
    resto = resto // 10
    a = c
    i += 1

if not adjacente:
    print("sim")
else:
    print("não")