### 7. Um brechó revende produtos usados, e fixa o preço de venda de cada produto conforme o valor 
### de sua aquisição: 
### Se o preço de aquisição de um produto é menor que R$ 50,00, ele deve ser vendido por um preço 45% maior, 
### caso contrário o lucro será de 30%. 
### Sabendo disso, faça um algoritmo que leia o valor de aquisição de um produto e mostre o seu valor de venda.

# Leitura do valor de aquisição do produto
preco_aquisicao = float(input("Digite o valor de aquisição do produto: R$"))

# Verificação do preço de venda conforme o valor de aquisição
if preco_aquisicao < 50:
    preco_venda = preco_aquisicao * 1.45  # Acréscimo de 45%
else:
    preco_venda = preco_aquisicao * 1.3  # Acréscimo de 30%

# Exibição do valor de venda
print("O valor de venda do produto é: R${:.2f}".format(preco_venda))
