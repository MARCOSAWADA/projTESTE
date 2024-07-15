#  34. Um produto vai sofrer aumento de acordo com a tabela abaixo. 
#  Leia o preço antigo, calcule e escreva o preço novo, 
#  e escreva uma mensagem em função do preço novo (de acordo com a segunda tabela).

# PREÇO ANTIGO            PERCENTUAL DE AUMENTO
# até R$ 50               5%
# entre R$ 50 e R$ 100    10%
# acima de R$ 100         15%

preco = float(input("digite o valor: "))

if preco <= 50:
    novo_preco = preco + (preco * 0.05)
elif preco > 50 and preco <=100:
    novo_preco = preco + (preco * 0.10)
else:
    novo_preco = preco + (preco * 0.15)


print(novo_preco)