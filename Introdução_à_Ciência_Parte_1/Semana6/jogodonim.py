def computador_escolhe_jogada(n,m):
    if n > m:
        for i in range(1, m+1):
            if (n-i) % (m+1) == 0:
                print(f"O computador tirou {i} peça.")
                return i
        return m
    elif n == m:
        print(f"O computador tirou {m} peça.")
        return m
    elif n < m:
        print(f"O computador tirou {n} peça.")
        return n

def usuario_escolhe_jogada(n,m):
    while True:
        a = int(input("Quantas peças você vai tirar? "))
        if a <= m and a <= n:
            print(f"Você tirou {a} peças.")
            return a
        else:
            print("Oops! Jogada inválida! Tente de novo.")


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    if n % (m+1) == 0:
        print("\nVocê começa!")
        while True:
            n = n - usuario_escolhe_jogada(n,m)
            if n == 0:
                print("Fim do jogo! O jogador ganhou!")
                break
            print(f"Agora restam apenas {n} peças no tabuleiro.\n")
            n = n - computador_escolhe_jogada(n,m)
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                break
            print(f"Agora restam apenas {n} peças no tabuleiro.\n")
    else:
        print("Computador começa!")
        while True:
            n = n - computador_escolhe_jogada(n,m)
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                break
            print(f"Agora restam apenas {n} peças no tabuleiro.\n")
            n = n - usuario_escolhe_jogada(n,m)
            if n == 0:
                print("Fim do jogo! O jogador ganhou!")
                break
            print(f"Agora restam apenas {n} peças no tabuleiro.\n")

def campeonato():
    print("Bem-vindo ao jogo do NIM! Escolha: ")
    a = 0
    while a != 1 and a != 2:
        a = int(input("1 - para jogar uma partida isolada \n2 - para jogar um campeonato "))
    if a == 2:
        print("Voce escolheu um campeonato!")
        for i in range(1,4):
            print(f'**** Rodada {i} ****')
            partida()
        print("\n**** Final do campeonato! ****")
        print("\nPlacar: Você 0 X 3 Computador")
    else:
        print(f'**** Rodada 1 ****')
        partida()

campeonato()