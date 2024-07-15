### 26. Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triangulo,
### se forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:
#• O comprimento de cada lado de um triangulo é menor do que a soma dos outros dois lados.
#• Chama-se equilátero o triângulo que tem três lados iguais.
#• Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
#• Recebe o nome de escaleno o triângulo que tem os três lados diferentes.


a=float(input("Digite o primeiro valor: "))
b=float(input("digite o segundo valor: "))
c=float(input("Digite o terceiro valor: "))

if a==b and a==c:
    print("o triangulo é equilátero")
elif a==b or a==c or b==c:
    print("O triangulo é isósceles")
elif a!=b and b!=c and a!=c:
    print("O triangulo é escaleno")