### 18. Seu João precisa fazer um empréstimo automático no aplicativo, 
### o banco aprova a transação de acordo com as seguintes condições: 
### Leia o salário de um trabalhador e o valor da prestação de um empréstimo. 
### Se a prestação for maior que 20% do salário imprima: Empréstimo não concedido, 
### caso contrário imprima: Empréstimo concedido

# Ler o salário do trabalhador e o valor da prestação do empréstimo
salario = float(input("Digite o salário do trabalhador: "))
prestacao_emprestimo = float(input("Digite o valor da prestação do empréstimo: "))

# Calcular 20% do salário
limite_prestacao = 0.20 * salario

# Verificar se a prestação excede 20% do salário
if prestacao_emprestimo > limite_prestacao:
    print("Empréstimo não concedido.")
else:
    print("Empréstimo concedido.")