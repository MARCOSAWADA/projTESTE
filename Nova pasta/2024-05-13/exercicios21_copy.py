# 21. Crie um programa que receba dois números. Calcule e mostre:
# • a soma dos números pares desse intervalo de números, incluindo os números digitados;
# • a multiplicação dos números ímpares desse intervalo, incluindo os digitados;



numero1=int(input("Digite um número: "))
numero2=int(input("Digite outro número: "))

soma_pares=0
mult_impar=1

numero_atual = min(numero1, numero2)
while numero_atual <= max(numero1, numero2):
    if numero_atual % 2 == 0:
        soma_pares+=numero_atual
    else:
        mult_impar*=numero_atual
    numero_atual+=1
print("A Soma dos números pares é: ", soma_pares)
print("A Multiplicação dos números ímpares é: ", mult_impar )
