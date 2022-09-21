time='Deus'
time.upper()
time.lower()

frase = 'ana gosta de banana'
frase.capitalize() #Coloca letra maiúscula na primeira palavra.

brazil = 'BRAZIL'
brazil.capitalize()

email = '   danielsottovia@gmail.com   '.strip() #Tira os espaços do começo e fim

a = frase.count('a') #conta o número de vezes que aparece a letra 'a'
print(a)

time = 'Eu torço para o Palmeiras'.replace('Palmeiras', 'São Paulo') #troca 'Palmeiras' por 'São Paulo'
print(time)

vari = frase.capitalize().center(80) #centraliza o texto
print(vari)

texto = 'Minha terra tem palmeiras onde gorgeia o mar'
num = texto.find('m') # Acha a primeira posição que 'm' aparece
print(num)

print(texto.find('ma'))

len(texto) #Tamanho do string

fruta = 'amora'
print(fruta[:4])
print(fruta[2:4])

tam = len("São Paulo é a maior cidade do Brasil")
print(tam)

frase = "São Paulo é a maior cidade do Brasil"
print(frase.find('ai'))
print(frase.count('o'))
print(frase.find('w'))