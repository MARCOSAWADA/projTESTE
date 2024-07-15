class Funcionario:
    def __init__(self, nome, sobrenome, horas_trabalhadas, valor_por_hora):
        self.nome = nome
        self.sobrenome = sobrenome
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_por_hora = valor_por_hora
    
    def nome_completo(self):
        print(f"Nome completo: {self.nome} {self.sobrenome}")
    
    def calcular_salario(self):
        salario = self.horas_trabalhadas * self.valor_por_hora
        print(f"Salário do mês: R$ {salario:.2f}")
    
    def incrementar_horas(self, horas):
        self.horas_trabalhadas += horas
        print(f"Horas trabalhadas atualizadas: {self.horas_trabalhadas}")
        

funcionario1 = Funcionario("João", "Silva", 160, 30.0)


funcionario1.nome_completo()
funcionario1.calcular_salario()

funcionario1.incrementar_horas(10)
funcionario1.calcular_salario()
   
