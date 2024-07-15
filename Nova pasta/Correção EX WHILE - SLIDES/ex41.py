# Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
# • o total a pagar com desconto de 10%;
# • o valor de cada parcela, no parcelamento de 3× sem juros;
# • a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
# • a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)

valor = float(input("DIGITE O VALOR DA VENDA: "))

porc =  valor * 10 / 100
pagvista = valor - porc
parcela = valor /3

comissao_avista = pagvista * 0.05
comissao_aprazo = valor * 0.05

print(f"COMPRA COM DESCONTO {pagvista}")
print(f"parcelas: {parcela:.3f}") 
print(f" \n comissao a vista: {comissao_avista}")
print(f"comissao a prazo: {comissao_aprazo}")