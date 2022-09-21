from Semana1 import matrizes

def soma_matrizes(A, B):
    num_lin = len(A)
    num_col = len(A[0])
    C = matrizes.criar_matriz(num_lin, num_col, 0)

    lin = 0
    while lin < num_lin:
        col = 0
        while col < num_col:
            C[lin][col] = A[lin][col] + B[lin][col]
            col += 1
        lin += 1

    return C

if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    B = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
    print(soma_matrizes(A, B))