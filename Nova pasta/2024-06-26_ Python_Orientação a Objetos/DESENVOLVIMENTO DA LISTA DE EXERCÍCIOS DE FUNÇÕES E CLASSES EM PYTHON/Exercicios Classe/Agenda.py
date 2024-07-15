class Agenda:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = ""

        
    def anotar_tarefa(self, tarefa):
        if self.dia <= 30 and self.mes <= 12:
            self.anotacao = tarefa
            print(f"Tarefa anotada para {self.dia}/{self.mes}/{self.ano}: {tarefa}")
        else:
            print("da naokkkkkkkk")

    def mostrar_anotacao(self):
        if self.anotacao:
            print(f"Anotação para {self.dia}/{self.mes}/{self.ano}: {self.anotacao}")
        else:
            print(f"Nenhuma anotação para {self.dia}/{self.mes}/{self.ano}")

# Exemplo de uso da classe
minha_agenda = Agenda(dia=331, mes=4, ano=2024)
minha_agenda.anotar_tarefa("Reunião às 14h")
minha_agenda.mostrar_anotacao()