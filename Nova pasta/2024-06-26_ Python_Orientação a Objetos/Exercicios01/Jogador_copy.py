class Jogador:
    def __init__(self, nome, numero, posicao):
        self.nome = nome
        self.numero = numero
        self.posicao = posicao
        self.nivel_tanque = 0  # inicialmente sem combustível
    
    def abastecer(self):
        # Simula o abastecimento, incrementando o nível do tanque de combustível
        self.nivel_tanque = 100  # considerando que o tanque foi abastecido ao máximo (100%)
        print(f"O jogador {self.nome} abasteceu o tanque.")
    
    def andar(self, distancia_km):

        if self.nivel_tanque > 0:

            consumo_por_km = 1.5
            litros_gastos = consumo_por_km * distancia_km
            self.nivel_tanque -= litros_gastos
            print(f"O jogador {self.nome} andou {distancia_km} km.")
        else:
            print(f"O jogador {self.nome} está sem combustível.")
    
    def verificar_nivel(self):

        return self.nivel_tanque
    
    def calcular_imposto(self, valor_carro):

        ipva = valor_carro * 0.025
        return ipva


jogador1 = Jogador("Neymar", 10, "Atacante")


jogador1.abastecer()


nivel_atual = jogador1.verificar_nivel()
print(f"Nível atual do tanque: {nivel_atual}%")


jogador1.andar(50)


nivel_atual = jogador1.verificar_nivel()
print(f"Nível atual do tanque: {nivel_atual}%")


valor_carro_jogador1 = 100000  # exemplo de valor do carro
imposto_ipva = jogador1.calcular_imposto(valor_carro_jogador1)
print(f"IPVA a pagar: R$ {imposto_ipva:.2f}")




# Explicação do código:
    
# 1. Método __init__:
# - O construtor __init__ inicializa os atributos nome, numero e posicao com os valores passados como argumentos quando um novo objeto Jogador é instanciado. O atributo nivel_tanque é inicializado como 0, indicando que o jogador começa sem combustível.

# 2. Método abastecer:
# - Simula o abastecimento do tanque de combustível, definindo o nível do tanque como 100 (máximo).

# 3. Método andar:
# - Simula o jogador andando uma distância especificada (distancia_km). Calcula quantos litros de combustível são gastos com base em um consumo específico por km (consumo_por_km). Atualiza o nível do tanque de acordo com o combustível gasto.

# 4. Método verificar_nivel:
# - Retorna o nível atual do tanque de combustível.

# 5. Método calcular_imposto:
# - Calcula o imposto (IPVA) do carro do jogador, que é 2,5% do valor do carro fornecido como argumento (valor_carro).


# Neste exemplo, a classe Jogador foi implementada para simular operações de um jogador de futebol, como abastecer o tanque de combustível (simulado com um valor fixo de 100%), andar uma distância especificada (com consumo simulado de combustível), verificar o nível de combustível e calcular o IPVA do carro do jogador. Cada objeto representa um jogador diferente com suas respectivas informações.