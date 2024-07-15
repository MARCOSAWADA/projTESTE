### 21. A nota final de um estudante e calculada a partir de três notas atribuídas entre o intervalo de 0 até 10, 
### respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. 
### A média das três notas mencionadas anteriormente obedece aos pesos: 
### Trabalho de Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. 

### De acordo com o resultado, mostre na tela se o aluno está 
### reprovado (média entre 0 e 2,9), 
### de recuperação (entre 3 e 5,9) ou se foi aprovado. 
### Faça todas as verificações necessárias.

# Ler as notas do aluno
nota_lab = float(input("Digite a nota do trabalho de laboratório (entre 0 e 10): "))
nota_semestral = float(input("Digite a nota da avaliação semestral (entre 0 e 10): "))
nota_final = float(input("Digite a nota do exame final (entre 0 e 10): "))

# Calcular a média ponderada das notas
media = (nota_lab * 2 + nota_semestral * 3 + nota_final * 5) / (2 + 3 + 5)

# Exibir a média do aluno
print("A média do aluno é:", media)

# Verificar a situação do aluno
if 0 <= media < 3:
    print("O aluno está reprovado.")
elif 3 <= media < 6:
    print("O aluno está em recuperação.")
else:
    print("O aluno está aprovado.")