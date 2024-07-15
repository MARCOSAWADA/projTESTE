# O gestor de uma rede de shoppings, precisa contratar um sistema para administrar o estacionamento, 
# a principal função do sistema é calcularTempo(). 
# Considere o valor mínimo de R$9,00 por hora e R$ 1,50 por hora adicional. 

# O principal argumento da função é o tempo utilizado em minutos, a função deve retornar o valor total. 

# Caso o usuário fique no estacionamento por menos de 15 minutos, o tempo utilizado não será cobrado.​



# def calcular_tempo(tempo_minutos):
#     preco_minimo = 9.00  
#     preco_adicional = 1.50  
#     tempo_horas = tempo_minutos / 60 

#     if tempo_minutos < 15:
#         return 0  

#     horas_inteiras = int(tempo_horas)
#     minutos_restantes = tempo_minutos % 60

#     if minutos_restantes > 0:
#         horas_inteiras += 1  

#     if horas_inteiras <= 1:
#         return preco_minimo  

#     preco_total = preco_minimo + (horas_inteiras - 1) * preco_adicional  
#     return preco_total


# tempo_utilizado = int(input("Informe o tempo utilizado no estacionamento (em minutos): "))
# valor_total = calcular_tempo(tempo_utilizado)
# print(f"O valor total a ser pago pelo tempo de estacionamento é: R$ {valor_total:.2f}")


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




def calcularTempo(horaEntrada, horaSaida):
    # Calcula o tempo de permanência em minutos
    entrada = horaEntrada.split(":")
    saida = horaSaida.split(":")
    minutosEntrada = int(entrada[0]) * 60 + int(entrada[1])
    minutosSaida = int(saida[0]) * 60 + int(saida[1])
    tempoPermanencia = minutosSaida - minutosEntrada

    # Calcula o valor a ser pago
    valorPorMinuto = 2
    valorTotal = valorPorMinuto * tempoPermanencia

    # Calcula os impostos
    pis = valorTotal * 0.0033
    cofins = valorTotal * 0.002
    icms = valorTotal * 0.17

    # Calcula o valor líquido a ser pago
    valorLiquido = valorTotal - (pis + cofins + icms)

    # Imprime o recibo
    print("Recibo do Cliente")
    print(f"Tempo de permanência: {tempoPermanencia} minutos")
    print(f"Valor total: R$ {valorTotal:.2f}")
    print(f"Valor líquido: R$ {valorLiquido:.2f}")
    print(f"PIS: R$ {pis:.2f}")
    print(f"COFINS: R$ {cofins:.2f}")
    print(f"ICMS: R$ {icms:.2f}")

# Exemplo de uso
calcularTempo("10:30", "11:30")
