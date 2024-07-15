class Carro:
    def __init__(self, modelo, marca, cor, ano, valor, consumo):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.nivel = 0
        self.consumo = consumo

    def abastecer(self, litros):
        self.nivel += litros

    def andar(self, distancia_km):
        litros_gastos = distancia_km / self.consumo
        if self.nivel >= litros_gastos:
            self.nivel -= litros_gastos
            print(f"O carro andou {distancia_km} km. Nível atual do tanque: {self.nivel:.2f} litros.")
        else:
            print("Não há combustível suficiente para percorrer essa distância.")

    def verificar_nivel(self):
        return self.nivel

    def calcular_imposto(self):
        ipva = self.valor * 0.025
        return ipva

# Exemplo de uso da classe
meu_carro = Carro(modelo="Fiesta", marca="Ford", cor="Azul", ano=2020, valor=30000, consumo=12)
meu_carro.abastecer(30)
meu_carro.andar(200)
print(f"Nível atual do tanque: {meu_carro.verificar_nivel():.2f} litros")
print(f"IPVA a pagar: R${meu_carro.calcular_imposto():.2f}")

