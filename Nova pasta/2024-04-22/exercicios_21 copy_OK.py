### 21. A nota final de um estudante e calculada a partir de três notas atribuídas entre o intervalo de 0 até 10, 
### respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. 
### A média das três notas mencionadas anteriormente obedece aos pesos: 
### Trabalho de Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. 

### De acordo com o resultado, mostre na tela se o aluno está 
### reprovado (média entre 0 e 2,9), 
### de recuperação (entre 3 e 5,9) ou se foi aprovado. 
### Faça todas as verificações necessárias.

laboratorio = float(input("digite a nota do laboratório: "))
semestral = float(input("digite a nota semestral: "))
final = float(input("digite a nota final: "))

media = ((laboratorio*2)+(semestral*3)+(final*5)) / 10

print("A média do aluno é:", media)

if media >= 0.0 and media <=2.9:
    print("reprovado")
elif media >= 3.0 and media <=5.9:
    print("recuperação")
else:
    print("APROVADO!")