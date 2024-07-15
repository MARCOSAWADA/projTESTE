class NF:
    def __init__(self, numero, tipo, serie, cnpj, razao_social, data, valor_produtos, icms, frete, ipi):
        self.numero = numero
        self.tipo = tipo
        self.serie = serie
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.data = data
        self.valor_produtos = valor_produtos
        self.icms = icms
        self.frete = frete
        self.ipi = ipi
        self.valor_total = 0
        
    def obterNumero(self):
        return self.numero
    
    def obterDataEmissao(self):
        return self.data
    
    def alterarRazaoSocial(self, nova_razao_social):
        self.razao_social = nova_razao_social
        print(f"Razão social alterada para: {self.razao_social}")
    
    def calcularValorTotal(self):
 
        self.valor_total = self.valor_produtos + self.icms + self.frete + self.ipi
        print(f"Valor total da NF calculado: R$ {self.valor_total:.2f}")


nf1 = NF(12345, 'Saída', 1, '12.345.678/0001-00', 'Empresa A', '2024-06-27', 1500.00, 200.00, 50.00, 100.00)


numero_nf = nf1.obterNumero()
print(f"Número da NF: {numero_nf}")


data_emissao_nf = nf1.obterDataEmissao()
print(f"Data de emissão da NF: {data_emissao_nf}")


nf1.alterarRazaoSocial("Nova Empresa A")


nf1.calcularValorTotal()
