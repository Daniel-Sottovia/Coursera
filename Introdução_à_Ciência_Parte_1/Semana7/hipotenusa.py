import math
def hipotenusa(i,j):
    hip = math.sqrt((i**2 + j**2))
    limp = int(hip)
    if hip - limp == 0:
        return hip
    else:
        return 0


def soma_hipotenusas(n):
    soma = 0
    i = 1
    lista = []
    while i <= n:
        j = 1
        while j <= n:
            a = hipotenusa(i,j)
            if a <= n and a != 0:
                lista.append(a)
            j += 1
        i += 1
    l = list(set(lista)) #tira os números repetidos da lista
    for y in l:
        soma = soma + y
    return soma
