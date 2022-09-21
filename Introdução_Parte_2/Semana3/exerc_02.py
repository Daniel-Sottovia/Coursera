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
