"""
*args e **kwargs
"""

#Trabalhando com *args
#O *args é um parametro que coloca todos os argumentos em uma tupla, mas deixa ele não obrigatório
#Exemplo:

def soma(*args):
        return sum(args)
        
print(soma())
print(soma(1))
print(soma(3, 4))

#Trabalhando com **kwargs
#O **kwargs é parecido com o *args, mas deixa os argumentos em um dicionário. 
# Também não são obrigatórios
#Exemplo:

def cores(**kwargs):
    return kwargs

cores_escolhidas = {"Carlos":"Azul", "Bianca":"rosa", "renato":"verde"}
print(cores(**cores_escolhidas))#aqui estamos fazendo o desempacotamento dos arquivos
