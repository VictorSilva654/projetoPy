"""
Lambdas, ou expressões lambdas, são funções sem nome, ou seja, funções anônimas
"""

#exemplo

#Função comum
def calc(valor1, valor2):
    return valor1 + valor2

print(calc(9, 54))

#Expressão Lambda
calcular = lambda num1, num2: num1 + num2
print(calcular(9, 54))
#Essa não é a forma mais correta de fazer a expressão lambda

#Função map
#A função map ela 'mapeia' elemento de um dado iterável (tupla, lista, etc) e aplica uma função
#Ela recebe dois parâmetros, a função e o iterável
#Nesse exemplo, vamos utilizar a lambda da forma mais correta

numeros = (2, 5, 7, 8, 9, 54, 80, 542, 356)
tupla_do_map = tuple(map(lambda numero: numero * 35, numeros))
#aqui criamos a função lambda, que pega um número e multiplica ele por 35
#o map mapeia cada dado da tupla e aplica essa função
print(tupla_do_map)

