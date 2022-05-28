"""
POO - Programação Orientada a Objetos no Python

Por padrão, os atributos da classe em Python são públicos. Para deixá-los privados, é necessário
usar o __ (duplo underline) antes do nome do atributo.

OBS: É apenas uma convenção, por que, ao contrário do Java, a gente consegue acessar os dados
de um atributo privado fora da classe.
"""

class Carro:

    #Método construtor (o self se refere a instancia da classe)
    #Quando referenciamos a instancia da classe e precisamos usar os atributos da classe, 
    #chamamos o método de Método de Instancia
    def __init__(self, marca, modelo, potencia_motor, carroceria):
        #aqui estamos declarando os atributos de instancia como privados
        self.__marca = marca
        self.__modelo = modelo
        self.__potencia_motor = potencia_motor
        self.__carroceria = carroceria

    #Quando não precisamos usar atributos da instancia, usamos um método de classe
    #Ele é usado com o decorador @classmethod
    #Aqui o cls referencia a própria classe
    @classmethod
    def carro_anda(cls):
        return "VRUUUMMMMM"
    
    #Podemos também usar um Método Estático, que não precia referenciar a classe
    #Ele é usado com o decorador @staticmethod
    @staticmethod
    def carro_buzina():
        return "BIII BIIIII"
    
    @staticmethod
    def passa_marcha():
        marcha = 1
        while marcha <=5:
            print(f"Passei a {marcha} marcha!")
            marcha = marcha + 1
            

carro1 = Carro("VolksWagen", "Up", "1.0", "Hatch")
#print(carro1.carro_anda())
#print(carro1.carro_buzina())

carro1.passa_marcha()
print(carro1.__dict__)

