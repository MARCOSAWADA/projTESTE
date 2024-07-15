# Escreva um programa, com uma função que necessite de um argumento.
# A função retornar o valor de caractere "P", se seu argumento for positivo,
# e "N", se seu argumento for zero ou negativo.


def argumento(n1):
    if n1 >0:
        return "P"
    else:
        return "N"

print(argumento(int(input("a: "))))