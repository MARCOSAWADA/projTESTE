# O gestor de uma rede de shoppings, precisa contratar um sistema para administrar o estacionamento, 
# a principal função do sistema é calcularTempo(). 
# Considere o valor mínimo de R$9,00 por hora e R$ 1,50 por hora adicional. 

# O principal argumento da função é o tempo utilizado em minutos, a função deve retornar o valor total. 

# Caso o usuário fique no estacionamento por menos de 15 minutos, o tempo utilizado não será cobrado.​



def calcular_tempo(tempo_minutos):
    preco_minimo = 9.00  # Valor mínimo por hora
    preco_adicional = 1.50  # Valor por hora adicional
    tempo_horas = tempo_minutos / 60  # Convertendo minutos para horas

    if tempo_minutos < 15:
        return 0  # Se o tempo utilizado for menor que 15 minutos, não há cobrança

    horas_inteiras = int(tempo_horas)
    minutos_restantes = tempo_minutos % 60

    if minutos_restantes > 0:
        horas_inteiras += 1  # Se houver minutos extras, arredonda para cima para a próxima hora

    if horas_inteiras <= 1:
        return preco_minimo  # Se o tempo utilizado for até 1 hora, retorna o valor mínimo

    preco_total = preco_minimo + (horas_inteiras - 1) * preco_adicional  # Calcula o preço total
    return preco_total

# Teste da função
tempo_utilizado = int(input("Informe o tempo utilizado no estacionamento (em minutos): "))
valor_total = calcular_tempo(tempo_utilizado)
print(f"O valor total a ser pago pelo tempo de estacionamento é: R$ {valor_total:.2f}")


# PARTE 2
# ______________________________________________________________________________________________________________________________


# Adicione na função calcularTempo() do sistema para estacionamento o valor dos impostos pago pelo cliente. 
# Considere o PIS: 0,33% , 
# COFINS: 0,20% e 
# ICMS: 17% no valor e 

# imprima o recibo do cliente de acordo com a saída abaixo:​

# __________________
# Tempo 4.0 horas
# PIS    R$ 0,45
# COFINS R$ 0,27
# ICMS     R$ 2,30
# IMPOSTOS R$ 3,01
# TOTAL    R$ 13,50
# __________________



