# #  Crie um algoritmo que apresente o seguinte resuldado:

# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *********
# **********
# ***********
# ************

n = int(input("Digite um numero, e que esse número seja o número 12 "))
for i in range(1, n + 1):
    print('*' * i)