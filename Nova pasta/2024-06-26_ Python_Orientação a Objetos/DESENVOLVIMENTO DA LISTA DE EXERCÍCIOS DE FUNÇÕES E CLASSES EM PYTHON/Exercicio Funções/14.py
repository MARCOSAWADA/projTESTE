# 14
def carro(kilometros, consumidos):
    kmlitro = kilometros / consumidos

    if kmlitro < 8:
        print("VGasta muito vende este carro!")
    elif kmlitro >= 8 and kmlitro <= 15:
        print("Êconomico!")
    elif kmlitro > 15:
        print("Super economico")
    else:
        print("erro sei la")