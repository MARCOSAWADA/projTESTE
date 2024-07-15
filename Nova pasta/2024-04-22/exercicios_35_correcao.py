# 35. Escreva um programa que, dado o valor da venda, 
# imprima a comissão que deverá ser paga ao vendedor. 
# Para calcular a comissão, considere a tabela abaixo:


# Venda mensal                                            Comissão
# Maior ou igual a R$100.000,00                           R$700,00 + 16% das vendas
# Menor que R$100.000,00 e maior ou igual a R$80.000,00   R$650,00 +14% das vendas
# Menor que R$80.000,00 e maior ou igual a R$60.000,00    R$600,00 +14% das vendas
# Menor que R$60.000,00 e maior ou igual a R$40.000,00    R$550,00 +14% das vendas
# Menor que R$40.000,00 e maior ou igual a R$20.000,00    R$500,00 +14% das vendas
# Menor que R$20.000,00                                   R$400,00 +14% das vendas


venda = float(input("digite o valor da casa: "))

if venda >= 100000:
    com= (venda * 16 / 100) + 700
    print(com)
elif venda < 100000 and venda >= 80000:
    com = (venda * 14 / 100) + 650
    print(com)
elif venda < 80000 and venda >= 60000:
    com = (venda * 14 / 100) + 600
    print(com)
elif venda < 60000 and venda >= 40000:
    com = (venda * 14 / 100) + 550
    print(com)
elif venda < 40000 and venda >= 20000:
    com = (venda * 14 / 100) + 500
    print(com)
else:
    com = (venda * 14 / 100)
    print(com)