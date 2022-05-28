"""
Raise é uma palavra reservada do Python, que lança uma exceção/erro para o console
"""

#Exemplo:
def tipo_certo(nome):
    if type(nome) is not str:
        raise TypeError("O tipo de entrada deve ser uma string!")
    print(f"Salve {nome}!")


tipo_certo("Eu mesmo")

