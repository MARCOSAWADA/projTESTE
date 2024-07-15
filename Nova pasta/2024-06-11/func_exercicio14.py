# Crie uma função que receba como argumento a potência elétrica de determinado aparelho e o tempo ligado e 
# retorne o consumo em KWh em seguida chame outra função para calcular a conta de energia,
# levando em consideração o consumo e o valor do KWh como argumentos.

def calcular_consumo(potencia, tempo_ligado):
    # Calcula o consumo em KWh
    consumo_kwh = (potencia * tempo_ligado) / 1000
    return consumo_kwh

def calcular_conta_energia(consumo_kwh, valor_kwh):
    # Calcula o valor da conta de energia
    valor_conta = consumo_kwh * valor_kwh
    return valor_conta

# Solicita os dados ao usuário
potencia_aparelho = float(input("Digite a potência elétrica do aparelho (em watts): "))
tempo_ligado = float(input("Digite o tempo ligado do aparelho (em horas): "))
valor_kwh = float(input("Digite o valor do KWh (em reais): "))

# Chama a função para calcular o consumo em KWh
consumo_kwh = calcular_consumo(potencia_aparelho, tempo_ligado)

# Chama a função para calcular a conta de energia
valor_conta_energia = calcular_conta_energia(consumo_kwh, valor_kwh)

# Exibe os resultados
print(f"\nConsumo em KWh: {consumo_kwh:.2f} KWh")
print(f"Valor da conta de energia: R${valor_conta_energia:.2f}")



# _________________________________________________________________________________________



def calcular_consumo(potencia, tempo_ligado):
    # Calcula o consumo em kWh
    consumo_kwh = (potencia * tempo_ligado) / 1000
    return consumo_kwh

def calcular_valor_conta(consumo_kwh, preco_kwh):
    # Calcula o valor da conta de energia elétrica
    valor_conta = consumo_kwh * preco_kwh
    return valor_conta

def calcular_conta_de_energia(potencia, tempo_ligado, preco_kwh):
    # Calcula o consumo em kWh
    consumo_kwh = calcular_consumo(potencia, tempo_ligado)
    
    # Calcula o valor da conta de energia elétrica
    valor_conta = calcular_valor_conta(consumo_kwh, preco_kwh)
    
    return consumo_kwh, valor_conta

# Exemplo de uso da função
potencia_aparelho = float(input("Digite a potência do aparelho em Watts: "))
tempo_ligado = float(input("Digite o tempo que o aparelho ficou ligado em horas: "))
preco_kwh = float(input("Digite o preço do kWh em reais: "))

consumo, valor_conta = calcular_conta_de_energia(potencia_aparelho, tempo_ligado, preco_kwh)

# Exibe o resultado
print("Consumo em kWh:", consumo)
print("Valor da conta de energia: R$ {:.2f}".format(valor_conta))
