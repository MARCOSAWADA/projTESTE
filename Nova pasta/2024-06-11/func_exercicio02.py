# Crie uma função para calcular a exponenciação, que necessite dois argumentos e apresente como resultado a potência.
# Sendo base elevado ao expoente.

def argumento(n1, n2):
    argumento=n1**n2
    return argumento


# x = argumento(3,2)
x1=int(input("a: "))
x2=int(input("b: "))
print(argumento(x1,x2))

x3 = argumento(int(input("1: ")), int(input("2: ")))
print(x3)