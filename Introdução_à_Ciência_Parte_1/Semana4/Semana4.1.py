"""
decrescente = True
anterior = int(input("Digite o primeiro número da sequência: "))

valor = 1
while valor != 0 and decrescente :
    valor = int(input("Digite o próximo número da sequência: "))
    if valor > anterior:
        decrescente = False
    anterior = valor

if decrescente:
    print("A sequência está em ordem decrescente! :-)")
else:
    print("A sequência não está em ordem decrescente! :-(")"""

meuCartao = int(input("Digite o número do seu cartão de crédito: "))

cartaolido = 1
encontreiMeuCartaoNaLista = False

while cartaolido != 0 and not encontreiMeuCartaoNaLista: #not False = True
    cartaolido = int(input("Digite o número do próximo cartão de crédito: "))
    if cartaolido == meuCartao:
        encontreiMeuCartaoNaLista = True

if encontreiMeuCartaoNaLista:
    print("EBA!!! Meu cartão está lá!")
else:
    print("Xi, meu cartão não está lá...")