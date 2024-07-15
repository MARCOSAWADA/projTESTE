### 19. Crie um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, 
### utilizando as seguintes formulas (onde h corresponde à altura):
### • Homens: (72.7∗ h)−58
### • Mulheres: (62,1∗ h)−44,7

# Ler a altura e o sexo da pessoa
altura = float(input("Digite a altura (em metros): "))
sexo = input("Digite o sexo (M para masculino, F para feminino): ")

# Calcular o peso ideal de acordo com o sexo
if sexo.upper() == 'M':
    peso_ideal = (72.7 * altura) - 58
    print("O peso ideal para um homem com altura de", altura, "metros é", peso_ideal, "quilos.")
elif sexo.upper() == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    print("O peso ideal para uma mulher com altura de", altura, "metros é", peso_ideal, "quilos.")
else:
    print("Sexo inválido. Por favor, insira M para masculino ou F para feminino.")