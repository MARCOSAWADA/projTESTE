cargo = input("Digite o cargo: ")
nome = input("Digite o nome: ")
email = input("Digite o email: ")
idade = int(input("Digite sua idade: "))

if idade >=18:
    print("Parabéns voce passou para a fase 1")
    curso = input("você possui curso na área?")
    if curso == "sim":
        print("Parabéns você passou para a fase 2")
        nota = float(input("Digite a nota da prova"))
        if nota >= 7:
            print("Parabéns voce passou para a fase final")
        else:
            print("Reprovou na etapa final")
    else:
        print("Obrigado pela participação")
else:
    print("obrigado pela participação")
            