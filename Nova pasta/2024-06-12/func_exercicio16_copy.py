# Crie uma função que receba múltiplos argumentos não nomeados,
# considere que a função receba numeros flutuantes como argumentos e 
# retorne a média dos argumentos.


def argumentos(*args):
    return sum(args)

res = argumentos(int(input("a: ")), int(input("b: ")), int(input("c: ")), int(input("d: ")))
res2 = res /4
print(res2)
