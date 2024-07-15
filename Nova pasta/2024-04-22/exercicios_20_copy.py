### 20. Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, 
### a soma de todos os seus algarismos. 
### Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1). 
### Se o número lido não for maior do que zero, o programa termina com a mensagem “Número inválido”.

# PARTE 2  DA QUESTÃO ESTÁ LÁ EMBAIXO.

numero = input("Digite um número inteiro maior que zero: ")

A = numero[0]
B = numero[1]
C = numero[2]

R = int(A) + int(B) + int(C)
print(R)

if R <= 0:
    print("número inválido")



# PARTE 2

### Crie um algoritmo que calcule a média ponderada das notas de 3 provas. 
### A primeira e a segunda prova têm peso 1 e a terceira tem peso 2. 
### Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado. 
### A nota para aprovação deve ser igual ou superior a 60 pontos.


#Agora, vamos criar o algoritmo para calcular a média ponderada das notas de 3 provas:



nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))


media = ((nota1 * 1 + nota2 * 1 + nota3 * 2) / 4) * 10 #=> pela nota que vale 0 a 100.


print("A média do aluno é:", media)


if media >= 60:
    print("O aluno foi aprovado.")
else:
    print("O aluno foi reprovado.")