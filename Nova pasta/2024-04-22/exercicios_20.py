### 20. Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, 
### a soma de todos os seus algarismos. 
### Por exemplo, ao número 251 corresponderá o valor 8 (2 + 5 + 1). 
### Se o número lido não for maior do que zero, o programa termina com a mensagem “Número inválido”.

# PARTE 2  DA QUESTÃO ESTÁ LÁ EMBAIXO.

# Ler um número inteiro maior que zero
numero = int(input("Digite um número inteiro maior que zero: "))

# Verificar se o número é maior que zero
if numero <= 0:
    print("Número inválido.")
else:
    # Inicializar a variável para armazenar a soma dos algarismos
    soma = 0
    
    # Calcular a soma dos algarismos
    while numero > 0:
        # Adicionar o último dígito à soma
        soma += numero % 10
        # Remover o último dígito do número
        numero //= 10
    
    # Exibir a soma dos algarismos na tela
    print("A soma dos algarismos é:", soma)


# PARTE 2

### Crie um algoritmo que calcule a média ponderada das notas de 3 provas. 
### A primeira e a segunda prova têm peso 1 e a terceira tem peso 2. 
### Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado. 
### A nota para aprovação deve ser igual ou superior a 60 pontos.


#Agora, vamos criar o algoritmo para calcular a média ponderada das notas de 3 provas:
#python
#Copy code



# Ler as notas das 3 provas
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))

# Calcular a média ponderada
media_ponderada = (nota1 * 1 + nota2 * 1 + nota3 * 2) / 4

# Exibir a média do aluno
print("A média do aluno é:", media_ponderada)

# Verificar se o aluno foi aprovado ou reprovado
if media_ponderada >= 60:
    print("O aluno foi aprovado.")
else:
    print("O aluno foi reprovado.")