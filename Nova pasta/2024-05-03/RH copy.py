
cargo = input("Digite o cargo: ")
nome_completo = input("Digite o nome do candidato: ")
idade = int(input("Digite a idade do candidato: "))
email = "Obrigado pela sua participação"
curso = input("Você possui curso de qualificação na área? [S][N]: ")
nota = float(input("Digite o valor da nota do candidato: "))
mensagem = "(Parabéns você passou de fase)"


if nota >= 7:
    print(nome_completo, "você passou na 1º fase do processo seletivo.")
    print(mensagem)
else:
    print(nome_completo, "você não atingiu a nota, você não esta apto. ")
    print(email)
    if curso == "S":
        print(nome_completo, "você passou para a segunda fase.")
        print(mensagem)
    elif curso == "N":
        print(nome_completo, "você não atendeu aos critérios para a segunda fase.")
        print(email)
if idade >= 18:
    print(nome_completo, "você esta apto para a etapa final.")
    print(mensagem)
else:
    print(nome_completo, "Você é menor de idade.")
    print(email)

