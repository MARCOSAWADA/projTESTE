x = 500
y = 0

try:
    res = x / y
    print(res)
except:
    print("Erro ao tentar realizar a divisão")
    y = int(input("Digite um valor pro Y Novamente:"))
finally:
    res = x / y
    print("RESULTADO: ", res)