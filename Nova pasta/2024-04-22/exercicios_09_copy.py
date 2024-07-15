### 09. Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. 
### Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.




numero = int(input("Digite um número: "))

raiz= numero**0.5

if numero >= 0:
    print("A raiz quadrada de", numero, "é", raiz)
else:
    print("Número inválido. O número deve ser positivo.")