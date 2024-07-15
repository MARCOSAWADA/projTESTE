class Agenda:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.anotacao = ""
    
    @staticmethod
    def validar_data(dia, mes, ano):
        # Verifica se o dia é válido para o mês e ano
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            return 1 <= dia <= 31
        elif mes in [4, 6, 9, 11]:
            return 1 <= dia <= 30
        elif mes == 2:
            # Verifica ano bissexto
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                return 1 <= dia <= 29
            else:
                return 1 <= dia <= 28
        else:
            return False
    
    def anotar_tarefa(self, anotacao):
        self.anotacao = anotacao
        print("Tarefa anotada com sucesso.")
    
    def mostrar_anotacao(self):
        if self.anotacao:
            print(f"Anotação: {self.anotacao}")
        else:
            print("Nenhuma anotação encontrada.")


agenda1 = Agenda(40, 6, 2024)


if Agenda.validar_data(agenda1.dia, agenda1.mes, agenda1.ano):
    print("Data válida.")
else:
    print("Data inválida.")

# Anotando uma tarefa
agenda1.anotar_tarefa("Reunião às 14:00")

# Mostrando a anotação
agenda1.mostrar_anotacao()

# Tentando anotar outra tarefa
agenda1.anotar_tarefa("Compras no mercado")

# Mostrando a nova anotação
agenda1.mostrar_anotacao()