"""
Herança de Classes
Polimorfismo
MRO - (Method Resolution Order)
"""

class Objeto:

    def __init__(self, nome, descricao):
        self.__nome = nome
        self.__descricao = descricao

    
    @property
    def fala_seu_nome(self):
        return f"Meu nome é {self._Objeto__nome}"

class Recipiente(Objeto):
    def __init__(self, nome, descricao, volume, cor):
        #Com o metodo super podemos acessar dados da classe mãe
        super().__init__(nome, descricao)
        self.__volume = volume
        self.__cor = cor

    #Quando sobrescrevemos um método da classe pai(override), estamos fazendo o polimorfismo
    @property
    def fala_seu_nome(self):
        return f"Aqui meu nome é Johnny"
    
class Copo(Recipiente, Objeto):
    #Nessa classe, Atribuímos duas classes pai, isso é chamado de Herança Múltipla
    #Declaramos primeiro a classe Recipiente, por isso os métodos dessa classe vão ser 
    # chamados primeiro, isso é chamado MRO (METHOD RESOLUTION ORDER)

    def __init__(self, nome, descricao, volume, cor):
        #Com o metodo super podemos acessar dados da classe mãe
        super().__init__(nome, descricao, volume, cor)


pote = Recipiente("Pote", "Um pote simples", "2L", "Roxo")
print(pote.__dict__)
print(pote.fala_seu_nome)

copo_americano = Copo("Copo Americano", "Um copo simples", "200 ML", "Transparente")
print(copo_americano.__dict__)
print(copo_americano.fala_seu_nome)
