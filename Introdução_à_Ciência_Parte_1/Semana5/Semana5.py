"""def soma(x,y):
    return x + y

print(soma(10,20))
print(soma(-20,100))

print(soma(12345,4321))
print(soma(20*32,soma(3,4)))"""

def soma(x,y,z):
    return x + y + z

print(soma(10,20,30))
print(soma(-20,100,200))

def multiplica(x,y,z):
    return x * y * z

print(multiplica(20, 30, 100))
print(multiplica(soma(20,40,7),soma(65,3,2),multiplica(2,3,4)))

def nome_do_seu_time():
    return "SPFC"

print(nome_do_seu_time())

def quieta():
    x = 10 + 20
    print(f"O valor calculado é {x}")

print(quieta())

def troca(x,y):
    aux = x
    x = y
    y = aux

x = 10
y = 20
troca(x, y)
print(f"x = {x} e y = {y}")

