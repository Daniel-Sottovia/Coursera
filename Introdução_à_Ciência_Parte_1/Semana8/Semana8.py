playlist_do_fabio = ["Adolescencia", "Pitanguinha", "Lance", "XVII" ]
lis = [3, 5, 4, 2, 62]

print(playlist_do_fabio)
print(len(playlist_do_fabio))
print(lis[0]) #As posições na lista começa com 0
print(playlist_do_fabio[0])
#print(playlist_do_fabio[4]) #4 está fora do limite da lista
print(playlist_do_fabio[-1])#Se coloca negativo, vai do último para o primeiro.
print(playlist_do_fabio[-2])
primos = [2, 3, 5, 7, 11, 13]
print(len(primos))

filme = ["O que é isso companheiro?", "Bruno Barreto", 1.83, 1997]
print(len(filme))
print(type(filme[0]))
print(type(filme[1]))
print(type(filme[2]))
print(type(filme[3]))

playlist_do_fabio.append("Strawberry Fields Forever")
print(len(playlist_do_fabio))

cartoes_amarelos = []
print(len(cartoes_amarelos))
cartoes_amarelos.append("Luís Fabiano")
cartoes_amarelos.append(1)

print(cartoes_amarelos)
cartoes_amarelos.append("Neymar Jr.")
cartoes_amarelos.append(78)

print(cartoes_amarelos)
print(cartoes_amarelos[2])
cartoes_amarelos[3] = 79 #Muda o valor da posição 3
print(cartoes_amarelos)