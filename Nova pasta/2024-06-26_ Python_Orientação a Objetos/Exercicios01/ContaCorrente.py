class ContaCorrente:
    def __init__(self, nome, cpf, numero, saldo):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito deve ser maior que zero.")
    
    def sacar(self, valor):
        if self.saldo > 0:
            if valor > 0 and valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para saque.")
        else:
            print("Saldo insuficiente para saque.")
    
    def imprimir_saldo(self):
        print(f"Saldo atual da conta: R$ {self.saldo:.2f}")

# Criando um objeto conta1 da classe ContaCorrente
conta1 = ContaCorrente("Maria Silva", "123.456.789-00", "001", 1000.0)

# Exemplo de acesso aos atributos e métodos
print(f"Nome do cliente: {conta1.nome}")
print(f"CPF do cliente: {conta1.cpf}")
print(f"Número da conta: {conta1.numero}")
conta1.imprimir_saldo()

# Realizando operações na conta
conta1.depositar(500.0)
conta1.imprimir_saldo()

conta1.sacar(200.0)
conta1.imprimir_saldo()

conta1.sacar(1500.0)  # Tentativa de saque com saldo insuficiente
conta1.imprimir_saldo()
