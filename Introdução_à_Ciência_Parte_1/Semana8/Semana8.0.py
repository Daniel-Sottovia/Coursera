frutas_exoticas = ["jaboticaba", "cupuaçu", "graviola"]

for fruta in frutas_exoticas:
    print(f"Eu adoro {fruta}")

primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

print(len(primos))

for x in primos:
    print(x * x)

for i in range(20):
    print(i)

for i in range(10, 20):
    print(i)

for i in range(0, 100, 2):
    print(i)

pares = range(0, 40, 2)
for i in pares:
    print(i)

numeros = range(100, 0, -5)
for x in numeros:
    print(x)

primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

for i in range(len(primos)):
    primos[i] = primos[i]**3
print(primos)

cubos_dos_primos = primos
print(cubos_dos_primos)

animais = ["gato", "cachorro", "papagaio", "arara", "jacaré"]
for x in animais:
    print(x)