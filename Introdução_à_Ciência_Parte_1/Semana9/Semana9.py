"""
Objetos e referências
"""

a = "banana"
print(a)
b = "banana"
print(b)
c = "maçã"
print(c)

print(a is b)
print(a is c)

a = [81, 82, 83]
b = [81, 82, 83]

print(a is b)

"""
Repetições e referências
"""

origlist = [45, 76, 34, 55]
print(origlist * 3)
print([origlist] * 3)

newlist = [origlist] * 3
print(newlist)

origlist[1] = 99
print(origlist)
print(newlist)
lista1 = ["carro", "ônibus", "barco", "bicicleta"]
lista2 = ["carro", "ônibus", "barco", "bicicleta"]
lista3 = ["carro", "barco"]

print(lista1 is lista2)