from Pessoa1 import Pessoa1
from Professor import Professor
from Aluno import Aluno

melhorprof = Professor(123,"THIAGO ALMEIDA",32,"Analista de Sistema / Filósofo de Boteco","TODAS",200,25000)


melhorprof.getDados()
print(melhorprof.lecionar())

# melhorprof.getDados()
# print(melhorprof.formacao2())

aluno1 = Aluno(matricula="A123", nome="Alice", idade=20, notas=[8, 9, 7], media="calcular_media")
print(f"{aluno1.nome} tem média {aluno1.calcular_media()}")


# professor1 = Professor(matricula="P456", nome="Prof. Bob", idade=40, formacao="Ph.D.", disciplina="Computer Science", cargahora=40, salario=80000)
# professor1.lecionar()
# print(professor1.lecionar())