def imprime_retangulo_vazado():
    largura = int(input("digite a largura: "))
    altura = int(input("digite a altura: "))
    n = 1
    while n <= altura:
        i = 1
        while i <= largura:
            if n == 1 or n == altura:
                print('#', end='')
            elif i == 1 or i == largura:
                print('#', end='')
            else:
                print(' ', end='')
            i +=1
        print()
        n += 1

imprime_retangulo_vazado()
