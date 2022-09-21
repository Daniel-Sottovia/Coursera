class Carro:
    def __init__(self, m, a, c, vm):
        self.modelo = m
        self.ano = a
        self.cor = c
        self.vel = 0
        self.maxV = vm # velocidade maxima

    def imprima(self):
        if self.vel == 0: # parado da para ver o ano
            print(f"{self.modelo} {self.cor} {self.ano}")
        elif self.vel < self.maxV:
            print(f"{self.modelo} {self.cor} indo a {self.vel} Km/h")
        else:
            print(f"{self.modelo} {self.cor} indo muito raaaaaapiiiiiidoooooo!")

    def acelera(self, v):
        self.vel = v
        if self.vel > self.maxV:
            self.vel = self.maxV
        self.imprima()

    def pare(self):
        self.vel = 0
        self.imprima()

def main():
    carro1 = Carro('brasília', 1968, 'amarela', 80)
    carro2 = Carro('fuscão', 1981, 'preto', 95)

    carro1.acelera(40)
    carro2.acelera(50)
    carro1.acelera(80)
    carro1.pare()
    carro2.acelera(100)

main()