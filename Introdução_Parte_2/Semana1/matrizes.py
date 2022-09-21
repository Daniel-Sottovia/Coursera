A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

def criar_matriz(num_linhas, num_colunas, valor):
     matriz = []
     for i in range(num_linhas):
          linha = []
          for j in range(num_colunas):
               linha.append(valor)

          matriz.append(linha)

     return matriz

#B = criar_matriz(5,8,0)
#print(B)

"Escrever um método que escreve uma linha embaixo da outra."

def le_matriz():
     lin = int(input("Digite o número de linhas da matriz: "))
     col = int(input("Digite o número de colunas da matriz: "))
     return criar_matriz(lin, col)

