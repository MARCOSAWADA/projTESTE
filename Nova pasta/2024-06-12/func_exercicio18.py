# Uma rede de churrascaria realiza promoções semanais e 
# precisa automatizar os descontos de acordo com o dia da semana 
# (terça-feira 10%, quarta-feira 15%, quinta-feira 20%). 

# Crie uma função que calcule o preço final do consumo por pessoa. 
# Considere a taxa de atendimento e o couvert, caso o cliente concorde com o pagamento. 

# Utilize argumentos nomeados **kwargs, Exemplo de chamada da função:​

# desconto(‘quinta-feira’, valor=99.90, taxa=0.10, couvert=15)​

# ______________________
# Conta S/ taxas: 79.92
# Conta C/ taxas:
#     Rodízio: 79.92
#     Taxa Serviço: 7.99
#     Couvert: 15
# TOTAL: R$ 102.91
# ______________________



# def desconto(dia_da_semana, valor, taxa=0, couvert=0):
#     # Definindo os descontos de acordo com o dia da semana
#     if dia_da_semana == 'terça-feira':
#         desconto_percentual = 0.1  # 10%
#     elif dia_da_semana == 'quarta-feira':
#         desconto_percentual = 0.15  # 15%
#     elif dia_da_semana == 'quinta-feira':
#         desconto_percentual = 0.2  # 20%
#     else:
#         desconto_percentual = 0  # Sem desconto por padrão
    
#     # Calculando o preço final com desconto
#     valor_com_desconto = valor * (1 - desconto_percentual)
    
#     # Calculando o valor total com taxa de atendimento e couvert
#     valor_total = valor_com_desconto * (1 + taxa) + couvert
    
#     return valor_total

# # Exemplo de chamada da função
# preco_final = desconto(dia_da_semana='quinta-feira', valor=99.90, taxa=0.10, couvert=15)
# print(f"Preço final: R$ {preco_final:.2f}")






# ________________________________________________________________________________________







# def desconto(dia_da_semana, valor, **kwargs):
#     # Definindo os descontos de acordo com o dia da semana
#     descontos = {
#         'terça-feira': 0.1,    # 10%
#         'quarta-feira': 0.15,  # 15%
#         'quinta-feira': 0.2    # 20%
#     }
    
#     # Verificando se o dia da semana está nos descontos definidos
#     desconto_percentual = descontos.get(dia_da_semana, 0)  # Default 0% se não estiver nos descontos
    
#     # Calculando o preço final com desconto
#     valor_com_desconto = valor * (1 - desconto_percentual)
    
#     # Obtendo os valores opcionais ou utilizando valores padrão
#     taxa = kwargs.get('taxa', 0)
#     couvert = kwargs.get('couvert', 0)
    
#     # Calculando o valor total com taxa de atendimento e couvert
#     valor_total = valor_com_desconto * (1 + taxa) + couvert
    
#     return valor_total

# Exemplo de chamada da função
# preco_final = desconto(dia_da_semana='quinta-feira', valor=99.90, taxa=0.10, couvert=15)
# print(f"Preço final: R$ {preco_final:.2f}")




# ________________________________________________________________________________________



def desconto(dia_da_semana, valor, taxa=0, couvert=0):
    # Definindo os descontos de acordo com o dia da semana
    if dia_da_semana == 'terça-feira':
        desconto_percentual = 0.1  # 10%
    elif dia_da_semana == 'quarta-feira':
        desconto_percentual = 0.15  # 15%
    elif dia_da_semana == 'quinta-feira':
        desconto_percentual = 0.2  # 20%
    else:
        desconto_percentual = 0  # Sem desconto por padrão
    
    # Calculando o preço final com desconto
    valor_com_desconto = valor * (1 - desconto_percentual)
    
    # Calculando o valor total com taxa de atendimento e couvert
    valor_total = valor_com_desconto * (1 + taxa) + couvert
    
    return valor_total

# Exemplo de chamada da função
preco_final = desconto(dia_da_semana='quinta-feira', valor=99.90, taxa=0.10, couvert=15)
print(f"Preço final: R$ {preco_final:.2f}")

