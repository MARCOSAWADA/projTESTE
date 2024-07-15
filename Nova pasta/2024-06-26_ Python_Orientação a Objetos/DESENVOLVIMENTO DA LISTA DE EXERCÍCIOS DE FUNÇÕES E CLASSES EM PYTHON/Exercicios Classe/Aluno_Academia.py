class Aluno_Academia:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        self.mensalidade = 120.00
        
    def calcular_IMC(self):
        altura_metros = self.altura / 100 
        imc = self.peso / (altura_metros ** 2)
        return imc
    
    def obter_valor_mensalidade(self):
        if self.idade < 18:
            return self.mensalidade * 0.8
        else:
            return self.mensalidade


aluno1 = Aluno_Academia("João", 17, 58, 185)


imc_aluno1 = aluno1.calcular_IMC()
print(f"IMC do aluno {aluno1.nome}: {imc_aluno1:.2f}")


mensalidade_aluno1 = aluno1.obter_valor_mensalidade()
print(f"Mensalidade do aluno {aluno1.nome}: R$ {mensalidade_aluno1:.2f}")


aluno2 = Aluno_Academia("Maria", 24, 70, 167)


imc_aluno2 = aluno2.calcular_IMC()
print(f"IMC da aluna {aluno2.nome}: {imc_aluno2:.2f}")


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