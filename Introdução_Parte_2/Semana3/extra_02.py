class Triangulo():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def lei_dos_cossenos(self):
        cos_a = (self.b ** 2 + self.c ** 2 - (self.a) ** 2) / (2 * (self.b) * (self.c))
        cos_b = (self.a ** 2 + self.c ** 2 - (self.b) ** 2) / (2 * (self.a) * (self.c))
        cos_c = (self.a ** 2 + self.b ** 2 - (self.c) ** 2) / (2 * (self.a) * (self.b))
        final = self.ordem([cos_a, cos_b, cos_c])
        return final

    def ordem(self, lista):
        tam = len(lista)
        cont = 0
        final = []
        while cont < tam:
            if cont == 0:
                final.append(lista[cont])
            elif cont == 1:
                if lista[cont] > final[0]:
                    final.insert(0, lista[cont])
                else:
                    final.append(lista[cont])
            else:
                if lista[cont] > final[0]:
                    final.insert(0, lista[cont])
                else:
                    if lista[cont] > final[1]:
                        final.insert(1, lista[cont])
                    else:
                        final.append(lista[cont])
            cont += 1
        return final

    def semelhantes(self, t2):
        if self.lei_dos_cossenos() == t2.lei_dos_cossenos():
            return True
        else:
            return False


t1 = Triangulo(2, 3, 5)
t2 = Triangulo(4, 6, 10)
print(t1.semelhantes(t2))


