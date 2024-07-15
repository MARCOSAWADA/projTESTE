class Carro:
    def __init__(self, modelo, marca, cor, ano, valor, consumo):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.nivel_tanque = 0  # nível inicial do tanque (em litros)
        self.consumo = consumo  # consumo de combustível por km (em litros/km)
    
    def abastecer(self):
        # Simula o abastecimento, incrementando o nível do tanque de combustível
        self.nivel_tanque = 50  # considerando que o tanque foi abastecido até metade (50 litros)
        print(f"O carro {self.marca} {self.modelo} foi abastecido.")
    
    def andar(self, distancia_km):
        # Simula o carro andando uma distância em km
        if self.nivel_tanque > 0:
            # Calcula quantos litros de combustível foram gastos
            litros_gastos = self.consumo * distancia_km
            self.nivel_tanque -= litros_gastos
            print(f"O carro {self.marca} {self.modelo} andou {distancia_km} km.")
        else:
            print(f"O carro {self.marca} {self.modelo} está sem combustível.")
    
    def verificar_nivel(self):
        # Retorna o nível atual do tanque de combustível
        return self.nivel_tanque
    
    def calcular_imposto(self):
        # Calcula o IPVA do carro (exemplo com 2.5% do valor do carro)
        ipva = self.valor * 0.025
        return ipva

# Criando um objeto carro1 da classe Carro
carro1 = Carro("Civic", "Honda", "Preto", 2020, 80000.00, 12.5)

# Abastecendo o tanque do carro
carro1.abastecer()

# Verificando o nível atual do tanque
nivel_atual = carro1.verificar_nivel()
print(f"Nível atual do tanque: {nivel_atual} litros")

# Simulando o carro andando uma distância
carro1.andar(100)

# Verificando o nível de combustível após andar
nivel_atual = carro1.verificar_nivel()
print(f"Nível atual do tanque: {nivel_atual} litros")

# Calculando o imposto do carro
imposto_ipva = carro1.calcular_imposto()
print(f"IPVA a pagar: R$ {imposto_ipva:.2f}")



# Explicação do código:
    
# 1. Método __init__:
# - O construtor __init__ inicializa os atributos modelo, marca, cor, ano, valor, nivel_tanque (inicializado como 0) e consumo (consumo de combustível por km em litros/km) com os valores passados como argumentos quando um novo objeto Carro é instanciado.

# 2. Método abastecer:
# - Simula o abastecimento do tanque de combustível, definindo o nível do tanque com um valor fixo (nesse caso, 50 litros, que é metade de um tanque hipotético).

# 3. Método andar:
# - Simula o carro andando uma distância especificada (distancia_km). Calcula quantos litros de combustível são gastos com base no consumo por km (consumo). Atualiza o nível do tanque de acordo com o combustível gasto.

# 4. Método verificar_nivel:
# - Retorna o nível atual do tanque de combustível.

# 5.Método calcular_imposto:
# - Calcula o imposto (IPVA) do carro, que é 2,5% do valor do carro (valor).



# Neste exemplo, a classe Carro foi implementada para simular operações de um carro, como abastecer o tanque de combustível, andar uma distância especificada (com consumo simulado de combustível), verificar o nível de combustível e calcular o IPVA do carro. Cada objeto representa um carro diferente com suas respectivas informações.