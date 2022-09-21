def n_primos(n):
    cont = 0
    for i in range(2,n+1):
         cont = cont + primo(i)
    return cont

def primo(n):
    i = 2
    mult = 0
    while i <= n:
        if n % i == 0:
            mult += 1
        i += 1
    if mult <= 1:
        return 1
    else:
        return 0
