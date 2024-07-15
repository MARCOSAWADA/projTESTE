# Escreva um programa com uma função chamada somaimposto.
# A função possui dois parâmetros formais:
# taxaimposto, que é a quantia de imposto sobre vendas expressa em porcentagem e 
# custo, que é o custo de um item antes do imposto.
# A função "altera" o valor de custo para incluir o imposto sobre vendas.
# Por fim deve retornar o novo valor para o usuario considerando o percentual do imposto.



def somaimposto(taxaimposto, custo):
    imposto = custo * (taxaimposto / 100)  # Calcula o valor do imposto
    custo_total = custo + imposto  # Adiciona o imposto ao custo original
    return custo_total  # Retorna o custo total com imposto

# Exemplo de utilização da função
taxa = float(input("Informe a taxa de imposto sobre vendas em porcentagem: "))
preco = float(input("Informe o custo do item antes do imposto: "))

novo_preco = somaimposto(taxa, preco)
print("O novo preço do item, incluindo o imposto de", taxa, "%, é:", novo_preco)
