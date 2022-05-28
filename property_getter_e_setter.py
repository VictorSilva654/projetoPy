"""
Getters e Setters em Python

"""


class Funcionario:

    def __init__(self, nome, sobrenome, funcao, setor, salario):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__funcao = funcao
        self.__setor = setor
        self.__salario = salario

    #em Python o getter é chamado de Property
    @property
    def nome(self):
        return self.__nome

    @property
    def sobrenome(self):
        return self.__sobrenome

    @property
    def funcao(self):
        return self.__funcao

    @property
    def setor(self):
        return self.__setor

    @property
    def salario(self):
        return self.__salario

    #Os setters são declarados com o nome do atributo com o decorador setter    

    @setor.setter
    def setor(self, novo_setor):
        self.__setor = novo_setor

    @funcao.setter
    def funcao(self, novo_funcao):
        self.__funcao = novo_funcao

    @salario.setter
    def salario(self, novo_salario):
        self.__salario = novo_salario

    @property
    def nome_completo(self):
        return self.nome + " " + self.sobrenome

func1 = Funcionario("Valter", "Mercado", "Fiscal", "Manutenção", 2300.00)
print(func1.nome)
print(func1.funcao)
print(func1.nome_completo)
print(func1.__dict__)

func1.funcao = "Gerente"
print(func1.__dict__)



    
