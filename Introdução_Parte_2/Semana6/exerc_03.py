def incomodam(n):
    if n <= 0:
        return ''
    else:
        return 'incomodam ' + incomodam(n-1)


def elefantes(n, c = 1):
    if n == 1:
        return f'{c} elefantes {incomodam(c)}muito mais\n' + elefantes(n-1, c + 1)
    elif n == 0:
        return ''
    else:
        if c == 1:
            return 'Um elefante incomoda muita gente\n' + elefantes(n-1, c+1)
        else:
            return f'{c} elefantes {incomodam(c)}muito mais\n{c} elefantes incomodam muita gente\n' + elefantes(n-1, c + 1)

print(elefantes(4))