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
    "nome": "William",
    "idade": "22",
    "cidade": "Campo Grande",
    "profissão": "Novo Emprego",
}

informacao_nova2 = {
    "nome": "Jão",
    "idade": "18",
    "cidade": "Campo Grande",
    "profissão": "Futuro Militar",
}

if "nova variavel" in informacao_nova:
    print