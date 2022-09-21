print(5 > 3)

print(18 == 9 * 2)

print(type(False))

x = 12312
print(type(x>0))
print(x > 0 and x**2 > 100) #é a primeira e a segunda coisa

print(x < 0 and x == 12312)

print(x<0 or x==12312) #é uma ou outra

print(not x > 0) #não é essa parada

print(not False) #não é falso, logo, é verdadeiro

print(not True) #não é verdadeiro, logo, é falso

print(not not True)

fizerSol = True
forFeriado = False
vouParaPraia = fizerSol and forFeriado
print(vouParaPraia)

forFeriado = True
vouParaPraia = fizerSol and forFeriado
print(vouParaPraia)

paitrocinio = False
rolarPromocao = True
vouAoShow = paitrocinio or rolarPromocao
print(vouAoShow)

y = 50
print((x > 0) and (not y == 50) or (x + y == 150))

#print(fruta=laranja) retorna NameError;
