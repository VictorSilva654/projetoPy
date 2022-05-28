"""
Funções de maior grandeza (Higher order Functions):

 - São funções que podem retornar outras funções, funções que os argumentos são funções, e até
 suportam variáveis da função.

 No Python, podemos ter funções dentro de funções, chamados de Nested Functions - Funções aninhadas ou
 Inner Functions.

"""

#Exemplo de Inner Function

def quem_sou_eu(nome):
    def idade(numero):
        return numero
    minha_idade = idade(23)
    return f"Olá {nome}, você tem {minha_idade} anos!"

print(quem_sou_eu("Denilson"))
