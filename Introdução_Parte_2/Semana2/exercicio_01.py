def maiusculas(frase):
    frase = frase.strip()
    tam = len(frase)
    cont = 0
    final = ''
    while cont < tam:
        if ord(frase[cont]) >= 65 and ord(frase[cont]) <= 90:
            final = final + frase[cont]
        cont += 1
    return final
