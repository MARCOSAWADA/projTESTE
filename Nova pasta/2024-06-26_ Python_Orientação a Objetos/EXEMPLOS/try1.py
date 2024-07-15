####TRATAMENTO DE EXCEÇÃO

x = 500
y = 0

#TENTE REALIZAR A OPERAÇÃO DE DIVISÃO
try:
    res = x / y
    print(res)
except:
    print("Erro ao tentar realizar a divisao")
    y = int(input("Digite Y novamente"))
finally:
    res = x / y
    print("RESULTADO : ",res)




