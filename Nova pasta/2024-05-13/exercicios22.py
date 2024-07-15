# 22. Escreva um programa que permita a qualquer aluno introduzir, pelo teclado, 
# uma sequência de notas (válidas no intervalo de 0 a 10) e que mostre na tela, como resultado, 
# a correspondente média aritmética. 
# O número de notas com que o aluno pretenda efetuar o cálculo não fornecido ao programa, 
# o qual terminará quando for introduzido um valor que não seja válido como nota de aprovação.

qntd_notas=int(input("Digite a quantidade de notas: "))
soma=0
cont=0
while cont < qntd_notas:
    notas=float(input("Digite suas notas: "))
    if notas < 0 and notas > 10:
        print("Valor digitado inválido")
        break
    else:
        print(notas)
        soma+=notas
        cont+=1
        media=soma/qntd_notas
print("A média das suas notas é: ", media)