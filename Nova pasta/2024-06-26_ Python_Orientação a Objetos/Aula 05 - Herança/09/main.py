from Compra import Compra
from Avista import Avista
from Parcelada import Parcelada

compra_avista = Avista(numero=1, produto="Celular", valor=1000, desconto=50)
compra_avista.calcular_valor_total()
print(f"Valor do celular com desconto é: {compra_avista.preco_com_desconto()}")

compra_parcelada = Parcelada(numero=2, produto="Notebook", valor=2000, numero_de_parcelas=3)
compra_parcelada.calcular_valor_total()
print(f"Valor das parcelas: {compra_parcelada.valor_das_parcelas()}")