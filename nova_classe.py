"""
Implementando uma nova classe para ser testada
"""

class Cantor:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def canta():
        return "Salve Jorge!"