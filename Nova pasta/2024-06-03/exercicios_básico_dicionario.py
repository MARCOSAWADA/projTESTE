informacao = {
    "mks": "Marcos Kaoru Sawada",
    "idade": "34",
    "cidade": "Apucarana",
    "profissão": "Desenvolvedor de Sistemas",
}

print("-" * 150)

print("total de dados a serem incluidos:" , (len(informacao)))

print("-" * 150)

dados = informacao['mks']
print(dados)
dados = informacao['idade']
print(dados)

print("-" * 150)

informacao["mks"] = "Sawada Kaoru Marcos"
print(informacao)

print("-" * 150)

informacao['nome2'] = 'wendrill'
informacao['email'] = 'willian@gmail.com'
informacao['telefone'] = '67 9 999-9999'
print(informacao)

print("-" * 150)

for dados in informacao:
    print(dados)

print("-" * 150)

print("totais de dados incluidos:" , (len(informacao)))

print("-" * 150)





# apartir do 5. usar while, for, input

informacao_nova = {
    "William": {"idade": 22, "cidade": "Campo Grande", "profissão": "Novo Emprego"},
    "Jão": {"idade": 17, "cidade": "Campo Grande", "profissão": "Futuro Militar"},
    "Cauã": {"idade": 18, "cidade": "Campo Grande", "profissão": "Militar"},
    "Robozão": {"idade": 39, "cidade": "Lisboa", "profissão": "Aposentando"}
}


for nome in informacao_nova:
    print(nome)

print("-" * 150)

nome = input("Digite um nome de um amigo:")
if nome in informacao_nova:
    print("O Amigo Esta na lista")
else:
    print("O Amigo Não esta na lista")


print("-" * 150)










traduzir = {
    "Hello": "Holla",
    "Oyaho": "Bom dia",
    "Good Morning": "Bom dia",
    "Bambam": "Biiiirlll",
}



traducao=input("Digite uma palavra dentro do dicionario traduzir: ")
if traducao in traduzir:
    print(traduzir[traducao])
else:
    print("PALAVRA NÃO EXISTE!")
