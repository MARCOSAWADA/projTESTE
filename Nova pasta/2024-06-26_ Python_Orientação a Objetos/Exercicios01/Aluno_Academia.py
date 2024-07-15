class Aluno_Academia:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = 120.00  # valor default
        
    def calcular_IMC(self):
        altura_metros = self.altura / 100  # convertendo altura para metros
        imc = self.peso / (altura_metros ** 2)
        return imc
    
    def obter_valor_mensalidade(self):
        if self.idade < 18:
            return self.mensalidade * 0.8  # desconto de 20% para menores de idade
        else:
            return self.mensalidade

# Criando um objeto aluno1 da classe Aluno_Academia
aluno1 = Aluno_Academia("João", 16, 70, 170)

# Calculando e exibindo o IMC do aluno
imc_aluno1 = aluno1.calcular_IMC()
print(f"IMC do aluno {aluno1.nome}: {imc_aluno1:.2f}")

# Obtendo e exibindo o valor da mensalidade do aluno
mensalidade_aluno1 = aluno1.obter_valor_mensalidade()
print(f"Mensalidade do aluno {aluno1.nome}: R$ {mensalidade_aluno1:.2f}")

# Criando outro objeto aluno2 da classe Aluno_Academia
aluno2 = Aluno_Academia("Maria", 20, 60, 165)

# Calculando e exibindo o IMC da aluna
imc_aluno2 = aluno2.calcular_IMC()
print(f"IMC da aluna {aluno2.nome}: {imc_aluno2:.2f}")

# Obtendo e exibindo o valor da mensalidade da aluna
mensalidade_aluno2 = aluno2.obter_valor_mensalidade()
print(f"Mensalidade da aluna {aluno2.nome}: R$ {mensalidade_aluno2:.2f}")




# Explicação do código:
    
# 1. Método __init__:
# - O construtor __init__ inicializa os atributos nome, idade, peso, altura e mensalidade (com um valor default de R$ 120,00) com os valores passados como argumentos quando um novo objeto Aluno_Academia é instanciado.

# 2. Método calcular_IMC:
# - Este método calcula o Índice de Massa Corporal (IMC) do aluno utilizando a fórmula 
# IMC=pesoaltura , onde a altura é convertida de centímetros para metros antes do cálculo.
#     altura2
 
# 3. Método obter_valor_mensalidade:
# - Este método retorna o valor da mensalidade do aluno. Se o aluno tiver menos de 18 anos (idade < 18), aplica-se um desconto de 20% na mensalidade.


# Neste exemplo, a classe Aluno_Academia foi implementada para calcular o IMC dos alunos e determinar o valor da mensalidade, aplicando um desconto para alunos menores de 18 anos. Cada objeto representa um aluno diferente com suas respectivas informações.