linha = 1
coluna = 1
while linha <= 10:
    while coluna <= 10:
        print(linha * coluna, end = "\t") # \t atua como a tecla tab, deixa mais organizado
        coluna += 1
    linha += 1
    print()
    coluna = 1

x = 1
cont = 0
while x < 3:
    y = 0
    while y <= 4:
        cont += 1
        print(cont)
        y = y + 1
    x = x + 1

fora = 5
while fora > 0:
    dentro = 0
    while dentro < fora:
        print("oi")
        dentro = dentro + 1
    fora = fora - 1
