# O gestor de uma rede de shoppings, precisa contratar um sistema para administrar o estacionamento, 
# a principal função do sistema é calcularTempo(). 
# Considere o valor mínimo de R$9,00 por hora e R$ 1,50 por hora adicional. 

# O principal argumento da função é o tempo utilizado em minutos, a função deve retornar o valor total. 

# Caso o usuário fique no estacionamento por menos de 15 minutos, o tempo utilizado não será cobrado.​



def calcular_tempo(tempo_minutos):
    preco_minimo = 9.00  
    preco_adicional = 1.50  
    tempo_horas = tempo_minutos / 60 

    if tempo_minutos < 15:
        return 0  

    horas_inteiras = int(tempo_horas)
    minutos_restantes = tempo_minutos % 60

    if minutos_restantes > 0:
        horas_inteiras += 1  

    if horas_inteiras <= 1:
        return preco_minimo  

    preco_total = preco_minimo + (horas_inteiras - 1) * preco_adicional  
    return preco_total


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



# print("ESTACIONAMENTO - IMPOSTOS")
# def imposto(calcular_tempo):
#     tabela = {}



# # def calcular_tempo():

# pis = 0.0033
# cofins = 0.002
# icms = 0.17

# pis = valor_total * 0.0033
# cofins = tempo_utilizado * 0.002
# icms = tempo_utilizado * 0.17

# total_impostos = preco_total + pis + cofins + icms

# print(total_impostos)
# print(f"PIS é:  {pis:.2f}")
# print(f"COFINS é: {cofins:.2f}")
# print(f"ICMS é: {icms:.2f}")