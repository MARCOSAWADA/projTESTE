# Crie uma função que armazene os dados de uma pessoa em um dicionário e imprima-os na tela.
# Utilize argumentos nomeados **kwargs, exemplo de saída:

# ______________________________________________

# data type or argument: <class 'dict'>
# firstname is John
# Lastaname is Wood
# Email is johnwood@nomail.com
# Country is Wakanda
# Age is 25
# Phone is 9876543210

# ______________________________________________

# print("Tipo de Dados ou Argumento")

# def dados_pessoais(**kwargs):
#     for chave, valor in kwargs.items():
#         print(f"{chave} : {valor}")

# dados = {
#     "NOME": "Pantera",
#     "SOBRENOME" : "Negra",
#     "EMAIL" : "black@panter.com",
#     "PAÍS" : "Wakanda",
#     "IDADE" : 25,
#     "WHATS" : 9876543210

# }

# dados_pessoais(**dados)



def dados_pessoa(**kwargs):
    
    pessoa = {}

    for chave in kwargs:
        pessoa[chave] = kwargs[chave]

    print("Dados da Pessoa: ")
    for chave in pessoa:
        print(f"{chave}: {pessoa[chave]}")


dados_pessoa(Nome="Pantera", Sobrenome="Negra", País="Wakanda", Idade=35, Whats="987654321")