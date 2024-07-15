# 19
def triangulo(num):
    for i in range(num + 1):
        print(" " * (num - i) + "*" * (i*2 - 1))

triangulo(4)