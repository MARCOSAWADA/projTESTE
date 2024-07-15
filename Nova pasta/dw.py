from asd import Pessoa
from asd import Edini
from asd import Date
# from datetime import datetime
# print(datetime.strftime('%Y/%m/%d %H:%M:%S'))

person = Pessoa("KAUAN", 18)
print(person.mandaroi())
print(person.mostraridade())

person2 = Pessoa("Wendril", 66)
print(person2.mostraridade())
print(person2.mandaroi())

meunome = Edini("Kauan")
print(meunome.faltas())

time = Date(2019)
print(time.dia())