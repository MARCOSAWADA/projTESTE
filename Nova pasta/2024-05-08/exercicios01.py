# Faça um algoritmo que receba um número e apresente a tabuada do
# mesmo ao final.

numero = int(input("Digite um número para exibir a tabuada: "))

# Inicializando o contador
i = 1

# Enquanto o contador for menor ou igual a 10
while i <= 10:
    # Calculando e exibindo o resultado
    resultado = numero * i
    print(numero, "x", i, "=", resultado)
    # Incrementando o contador
    i += 1