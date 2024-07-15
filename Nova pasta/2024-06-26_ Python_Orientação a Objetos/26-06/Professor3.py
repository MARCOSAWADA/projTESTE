class Professor3:
    def __init__(self,matricula,nome,cpf,idade): 
        self.mat = matricula
        self.name = nome
        self.cpf = cpf
        self.age = idade

    
    def hello(self): 
        print(f" Olá {self.name}")

    def mostrardados(self): 

        print(f" Matricula: {self.mat}")
        print(f" Nome: {self.name}")
        print(f" CPF: {self.cpf}")
        print(f" IDADE: {self.age}")

prof = Professor3("1234", "Thiago", "123456789", "987654321")
prof.hello

