### 30. Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma 
taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%). Crie um programa 
em que o usuário entre com o valor e o estado destino do produto e o programa retorne o preço
final do produto acrescido do imposto do estado em que ele será vendido. Se o estado digitado 
não for válido, mostrar uma mensagem de erro.
    
print("Este programa calcula o preço final de um produto com base no valor e no estado destino.")

# Definindo as taxas de imposto para cada estado
taxas_imposto = {
    "MG": 0.07,
    "SP": 0.12,
    "RJ": 0.15,
    "MS": 0.08
}

# Leitura do valor e do estado destino do produto
valor_produto = float(input("Digite o valor do produto: "))
estado_destino = input("Digite a sigla do estado destino (MG, SP, RJ, MS): ").upper()

# Verificando se o estado destino é válido e calculando o preço final
if estado_destino in taxas_imposto:
    taxa_imposto = taxas_imposto[estado_destino]
    preco_final = valor_produto * (1 + taxa_imposto)
    print(f"O preço final do produto no estado {estado_destino} é R$ {preco_final:.2f}.")
else:
    print("Erro: Estado destino inválido. Por favor, digite uma sigla de estado válida.")
