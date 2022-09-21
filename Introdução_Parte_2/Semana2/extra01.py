def conta_letras(frase, contar='vogais'):
    tam = len(frase)
    cont = 0
    total = 0
    while cont < tam:
        if contar == 'vogais':
            if frase[cont].lower() in ['a','e','i','o','u']:
                total += 1
        elif contar == 'consoantes':
            if frase[cont].lower() in ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','x','w','y','z']:
                total += 1
        cont += 1

    return total
