def remove_repetidos(lista):
    final = []
    for i in lista:
        if i not in final:
            final.append(i)
    return reordenar(final)

def reordenar(lista):
    final = []

    for i in lista:
        for x in lista:
            if i <= x:
                if i not in final:
                    if len(final) == 0:
                        final.append(i)
                    else:
                        for num in range(0,len(final)):
                            if i < final[num]:
                                if i not in final:
                                    final.insert(num, i)
                            else:
                                if i not in final:
                                    final.append(i)
    return final

lista = [7,3,33,12,3,3,3,7,12,100]
print(remove_repetidos(lista))
