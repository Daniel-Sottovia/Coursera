primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

print(primos[1:2])

print(primos[2:7])

print(len(primos))

print(primos[0:12])

print(primos[12:25])

print(primos[:12])

print(primos[12:])

final = primos[12:]

print(final)

lista1 = ["vermelho", "verde", "azul"]
print(lista1)
lista2 = lista1
print(lista2)
lista2[0] = 'rosa'
print(lista2)


def clone(lista):
    clone = []
    for objeto in lista:
        clone.append(objeto)
    return clone

print(clone(lista2[1:]))
lista1 = ["vermelho", "verde", "azul"]
lista2 = lista1[:]

lista2[0] = "rosa"

print(lista1)
print(lista2)

print("rosa" in lista1)
print("rosa" in lista2)

if "rosa" in lista1:
    print("está")
if "vermelho" in lista1:
    print("está")
else:
    print("faltou")

print([1, 2] + [3, 4])
print([4,3,4,5,2]+[2,4,2,4,5,6])

a = [1,2,3]
b = [4,5,6]

print(a + b)
print(b + a)
print(b + a + b)

a.append("gato")
print(a)

b = a + [5]
print(b)
print(a)

a = [1,2,3]
a_triplicado = a * 3
print(a_triplicado)

b_quintuplicado = b * 5
print(b_quintuplicado)
print(len(b_quintuplicado))

a = [1,2,3]

del(a[1])
print(a)

lista = ['a', 'b', 'c', 'd', 'e', 'f']
print(lista)
del lista[1:5]
print(lista)

alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print(len(alfabeto))

carnes = ["picanha", "alcatra", "filé mignon", "cupim"]
carnes2 = carnes
carnes2.append("ponta de alcatra")
print(carnes)
print(carnes2)

rec = [0,2]
for i in range(0,len(rec)):
    print(i)