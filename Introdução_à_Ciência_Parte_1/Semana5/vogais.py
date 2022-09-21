def vogal(letra):
    letra = letra.lower()
    vogais = ['a','e','i','o','u']
    for vog in vogais:
        if letra == vog:
            return True
    return False
