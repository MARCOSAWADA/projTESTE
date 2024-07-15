from Pessoa2 import Pessoa2
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

pessoa_fisica = PessoaFisica(nome="João", telefone="123456789", email="joao@example.com", endereco="Rua A", cpf="123.456.789-00")
pessoa_fisica.negociar()
pessoa_fisica.comprar()

print("___"*9)

pessoa_juridica = PessoaJuridica(nome="Empresa XYZ", telefone="987654321", email="contato@xyz.com", endereco="Avenida B", cnpj="12.345.678/0001-99")
pessoa_juridica.negociar()
pessoa_juridica.vender()