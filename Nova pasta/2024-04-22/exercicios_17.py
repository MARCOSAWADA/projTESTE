### 17. Em uma empresa paga-se R$ 40,50 a hora e recolhe-se para o imposto de renda 11% dos salários acima de R$ 2500,00. 
### Dado o número de horas trabalhadas por um funcionário, informar o valor do seu salário líquido.

# Definir o valor pago por hora e o limite para o imposto de renda
valor_por_hora = 40.50
limite_imposto_renda = 2500.00

# Ler o número de horas trabalhadas
horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))

# Calcular o salário bruto
salario_bruto = valor_por_hora * horas_trabalhadas

# Verificar se o salário ultrapassa o limite para o imposto de renda
if salario_bruto > limite_imposto_renda:
    # Calcular o imposto de renda
    imposto_renda = 0.11 * (salario_bruto - limite_imposto_renda)
else:
    imposto_renda = 0

# Calcular o salário líquido
salario_liquido = salario_bruto - imposto_renda

# Exibir o salário líquido
print("O salário líquido é R$", salario_liquido)