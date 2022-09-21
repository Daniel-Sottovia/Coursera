def criar_lista():
    lis = []
    while True:
        a = int(input("Digite um número: "))
        if a == 0:
            break
        lis.append(a)
    fic = inverter(lis)
    for i in fic:
        print(i)

def inverter(x):
    lis = []
    tamanho = len(x) - 1
    while tamanho >= 0:
        lis.append(x[tamanho])
        tamanho = tamanho - 1
    return lis

criar_lista()
