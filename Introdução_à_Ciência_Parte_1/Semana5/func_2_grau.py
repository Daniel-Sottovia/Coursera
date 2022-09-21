import math

def delta(a,b,c):
    return (b ** 2) - (4 * a * c)

def condicao(a,b,c):
    if delta(a,b,c) < 0:
        return "Delta é negativo, não há raiz real."
    else:
        return delta(a,b,c)

def raiz(a,b,c):
    resps1 = (-b + math.sqrt(condicao(a,b,c)))/(2*a)
    resps2 = (-b - math.sqrt(condicao(a,b,c)))/(2*a)
    if resps1 == resps2:
        return f"Raiz única {resps1}"
    else:
        return f"Raízes da equação {resps1} e {resps2}"

print(raiz(2,3,-9))
