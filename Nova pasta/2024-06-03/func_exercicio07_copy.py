# Crie uma função que efetue o cálculo do salário e como retorno teremos o valor a ser pago
# conforme o numero de horas trabalhadas. 
# Considere a carga horario de 40h por semana como salário base,
# caso ultrapasse o limite de 40h o funcionário deve receber 50% a mais por hora excedente.



# Claro! Abaixo está uma função em Python que calcula o salário com base no número de 
# horas trabalhadas, considerando a carga horária de 40 horas por semana e pagando 50% 
# a mais por hora excedente:



# Esta função `calcular_salario` recebe o número de horas trabalhadas como entrada. 
# Se as horas trabalhadas excederem 40 horas por semana, a função calcula o salário para 
# as horas excedentes, pagando 50% a mais por hora excedente. 
# Em seguida, calcula o salário total somando o salário base e o salário por hora excedente. 

# Se as horas trabalhadas forem iguais ou inferiores a 40 horas, o salário é calculado apenas 
# com base no salário base por hora.



def calcular_salario(horas_trabalhadas):
    salario_base_por_semana = 40 * salario_hora_base
    salario_excedente_por_semana = 0
    
    if horas_trabalhadas > 40:
        horas_excedentes = horas_trabalhadas - 40
        salario_excedente_por_semana = horas_excedentes * (salario_hora_base * 1.5)
        salario_total = salario_base_por_semana + salario_excedente_por_semana
    else:
        salario_total = horas_trabalhadas * salario_hora_base
    
    return salario_total


salario_hora_base = float(input("Informe o salário por hora base: "))


horas_trabalhadas = float(input("Informe o número de horas trabalhadas na semana: "))


salario_total = calcular_salario(horas_trabalhadas)
print("O salário total a ser pago é: R$", salario_total)



