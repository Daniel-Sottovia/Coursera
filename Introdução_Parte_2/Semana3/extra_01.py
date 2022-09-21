class Triangulo():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimetro(self):
        self.perimetro = int(self.a + self.b + self.c)
        return self.perimetro

    def tipo_lado(self):
        if self.a == self.b:
            if self.a == self.c:
                return 'equilátero'
            else:
                return 'isósceles'
        else:
            if self.b == self.c:
                return 'isósceles'
            elif self.a == self.c:
                return 'isósceles'
            else:
                return 'escaleno'

    def retangulo(self):
        if self.a > self.b and self.a > self.c:
            soma = (self.b)**2 + (self.c)**2
            if (self.a**2) == soma:
                return True
            else:
                return False

        elif self.b > self.a and self.b > self.c:
            soma = (self.a)**2 + (self.c)**2
            if (self.b**2) == soma:
                return True
            else:
                return False

        elif self.c > self.a and self.c > self.b:
            soma = (self.a)**2 + (self.b)**2
            if (self.c**2) == soma:
                return True
            else:
                return False

        else:
            return False