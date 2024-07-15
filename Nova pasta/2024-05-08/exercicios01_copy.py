# Faça um algoritmo que receba um número e apresente a tabuada do
# mesmo ao final.

numero = int(input("Digite um número para exibir a tabuada: "))


contador = 1


while contador <= 10:
    
    resultado = numero * contador
    print(numero, "x", contador, "=", resultado)

    contador = contador + 1