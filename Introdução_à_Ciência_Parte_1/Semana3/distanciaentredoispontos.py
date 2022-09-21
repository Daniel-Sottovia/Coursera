import math

a = int(input('Informe a coordenada em x: '))
b = int(input('Informe a coordenada em y: '))
print(f'Ponto 1: ({a},{b})')
c = int(input('Informe a coordenada em x: '))
d = int(input('Informe a coordenada em y: '))
print(f'Ponto 2: ({c},{d})')
distancia = math.sqrt((a-c)**2 + (b-d)**2)

if distancia >= 10:
    print('longe')
else:
    print('perto')