# Crie um função que receba múltiplos argumentos não nomeados, considere que a função receba números inteiros
# como argumentos e retorne a soma dos argumentos.

# def argumentos(n1, *args):
#     n=0
#     for i in args:
#         n1+=i
#     return(f"numeros : {args}, resultado: {n1}")

# x= argumentos(10,20,30,40)
# print(x)



def argumentos(*args):
    return sum(args)

res = argumentos(10,20,30,40)
print(res)





# recebe numeros inteiros como argumentos

# def soma recebe args
# nome de uma funcao resultaoo 1 = soma e qauis os apraremtnso 1 2 3
# resultaod rescve 1 2 520 3
# resultao3  7 41 52 93 99 

# chamar a guncao soma e criar as variaves e as funcoes


# receba numeros e retorne os numeros


# kwargs indicar a chave e o valor
# dicionario ou 

# args
# tuplas