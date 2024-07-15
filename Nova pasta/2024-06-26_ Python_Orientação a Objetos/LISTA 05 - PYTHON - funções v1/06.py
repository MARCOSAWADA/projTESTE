# Reverso do número. Faça uma função que retorne o reverso de um número informado.
# Por exemplo: 127 -> 721.

def inverter_numero(numero):
    print (str(numero)[::-1])

inverter_numero(5312)

numero_original = 127
numero_invertido = inverter_numero(numero_original)
print(f"O reverso do número {numero_original} é {numero_invertido}.")

def inverter(num):
    num = str(num)
    invertido = "".join(reversed(num))
    print(invertido)

inverter(1234)


def reverter(l):
  #Se a l estiver vazia apenas retorna []
  if len(l) == 0: return []
  #Devolve o último elemento de l mais o reverso da fatia que vai do 
  #primeiro elemento ao penúltimo elemento inclusive
  return [l[-1]] + reverter(l[:-1]) 

print('Digite uma lista de inteiros separados por espaço:')
sequencia = [int(e) for e in input().split(" ")]

sequencia = reverter(sequencia)

print(" ".join([str(e) for e in sequencia]))


print('Digite uma lista de inteiros separados por espaço:')
sequencia = [int(e) for e in input().split(" ")]

sequencia.reverse()

print(" ".join([str(e) for e in sequencia]))