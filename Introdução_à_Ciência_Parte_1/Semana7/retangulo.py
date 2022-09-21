def imprime_retangulo_cheio():
    largura = int(input("digite a largura: "))
    altura = int(input("digite a altura: "))
    n = 1
    while n <= altura:
        i = 1
        while i <= largura:
            print('#', end='')
            i +=1
        print()
        n += 1

imprime_retangulo_cheio()