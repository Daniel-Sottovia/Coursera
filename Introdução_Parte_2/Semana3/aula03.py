class Carro:
    def __init__(self, ano, modelo, cor, velocidade):
        self.ano = ano
        self.modelo = modelo
        self.cor = cor
        self.velocidade = velocidade

    def acelera(self, acel):
        self.velocidade = self.velocidade + acel


meu_carro = Carro(ano=1997, modelo='Parati', cor='branco', velocidade=30)
print(meu_carro)
meu_carro.ano += 10
print(meu_carro.ano)
meu_carro.acelera(5)
print(meu_carro.velocidade)