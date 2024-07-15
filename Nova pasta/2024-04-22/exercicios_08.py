### 08. Faça um Programa que receba 3 entradas de dados e informe qual tipo de dados está 
### armazenado na variável se é do tipo: int, float ou string

# Leitura das entradas de dados
entrada1 = input("Digite o primeiro valor: ")
entrada2 = input("Digite o segundo valor: ")
entrada3 = input("Digite o terceiro valor: ")

# Verificação do tipo de dado e exibição
print("Tipo de dado da primeira entrada:", type(entrada1).__name__)
print("Tipo de dado da segunda entrada:", type(entrada2).__name__)
print("Tipo de dado da terceira entrada:", type(entrada3).__name__)
