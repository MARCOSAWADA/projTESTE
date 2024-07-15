# Crie um função que receba múltiplos argumentos não nomeados, considere que a função receba números inteiros
# como argumentos e retorne a soma dos argumentos.

def media (*args):
    if not args:
        return 0
    soma = sum(args)
    quantidade = len(args)
    return soma / quantidade

result = media(100, 100, 100)
print(result)




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