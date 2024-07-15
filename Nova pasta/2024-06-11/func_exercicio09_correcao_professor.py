# O gestor de uma rede de shoppings, precisa contratar um sistema para administrar o estacionamento, 
# a principal função do sistema é calcularTempo(). 
# Considere o valor mínimo de R$9,00 por hora e R$ 1,50 por hora adicional. 

# O principal argumento da função é o tempo utilizado em minutos, a função deve retornar o valor total. 

# Caso o usuário fique no estacionamento por menos de 15 minutos, o tempo utilizado não será cobrado.​




# CORREÇÃO DO PROFESSOR LUIS



def calcular_tempo(tempo_em_minuto):
    valor_minuto_por_hora = 9.00
    valor_adicional_por_hora = 1.50

    if tempo_em_minuto < 15:
        return 0.00
    
    horas_completas = tempo_em_minuto // 60
    minutos_restantes = tempo_em_minuto % 60

    if minutos_restantes > 0:
        horas_completas += 1
    
    if horas_completas == 1:
        total = valor_minuto_por_hora
    else:
        total = valor_minuto_por_hora + (horas_completas -1) * valor_adicional_por_hora
        return total
    
tempo_utilizado = int(input("Digite o tempo em minutos: "))
valor_total = calcular_tempo(tempo_utilizado)
print(f"O valor total a ser pago é:{valor_total:.2f}")


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


# def calcular_tempo(tempo_utilizado):

#     tempo_utilizado = int(input(4))
