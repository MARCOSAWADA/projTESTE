# 15
import random
def embaralhar(palavra):
    aleatorio = list(palavra)
    random.shuffle(aleatorio)
    aleatorio = "".join(aleatorio)
    print(aleatorio)

embaralhar("Toxicysm")