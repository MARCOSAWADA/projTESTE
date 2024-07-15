# Um comerciante possui uma loja de artigos de R$ 1,99. 
# Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu uma tabela que contém o número de itens 
# que o cliente comprou e ao lado o valor da conta. 
# Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está levando e olhar na tabela de preços. 

# Você foi contratado para desenvolver uma função que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, 
# conforme o exemplo abaixo:​

# ________________________________________________

# Lojas Quase Dois - Tabela de preços
# 1 - R$ 1.99
# 2 - R$ 3.98
# ...
# 50 - R$ 99.50

# ________________________________________________


# criar um funcao variavel preco por item 1,99

# em formato de lista
# primeira coluna itens e valor

print("lojas quase dois - Tabela de preços")
def montar_tabelapreco():
    tabela = {}
    preco_por_item = 1.99
    for quantidade in range(1,51):
        total = quantidade * preco_por_item
        tabela[quantidade] = total
    return tabela
    
tabela = montar_tabelapreco()
for quantidade, total in tabela.items():
    print(quantidade, ":" , total)
    print(f"{quantidade} : {total:.2f}")
