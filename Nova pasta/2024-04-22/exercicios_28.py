### 28. Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. 
### As condições para aposentadoria são:
# • Ter pelo menos 65 anos,
# • Ou ter trabalhado pelo menos 30 anos,
# • Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

print("Este programa verifica se um trabalhador pode se aposentar.")

# Leitura da idade e tempo de serviço do trabalhador
idade = int(input("Digite a idade do trabalhador: "))
tempo_de_servico = int(input("Digite o tempo de serviço do trabalhador (em anos): "))

# Verificação das condições para aposentadoria
if idade >= 65:
    print("O trabalhador pode se aposentar.")
elif tempo_de_servico >= 30:
    print("O trabalhador pode se aposentar.")
elif idade >= 60 and tempo_de_servico >= 25:
    print("O trabalhador pode se aposentar.")
else:
    print("O trabalhador não pode se aposentar ainda.")