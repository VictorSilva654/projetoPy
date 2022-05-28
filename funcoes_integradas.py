"""
Funções integradas em Python

#Função filter
#a função filter filtra dados, ela recebe dois dados: uma função e um iterável

nomes = ['João', 'Maria', 'José', 'Abner', 'Welington']
lista_filtrada = list(filter(lambda nome: len(nome) >= 5, nomes))
print(lista_filtrada)

#Generator Expression
#Generators são comprehensions de tuplas

tupla = (2, 6, 4, 74, 35, 56, 21, 0, 4, 3, 49, 57, 67)
primos = (numero % 2 == 0 for numero in tupla)

for num in primos:
    print(num)

#Min e #Max
#Min retorna o menor valor de um iterável ou entre dois valores, e o max retorna o maior

lista_nomes = ("Mercúrio", "Vênus", "Marte", "Júpiter", "Saturno", "Terra", "Plutão")
print(min(lista_nomes)) #Aqui vai retornar o menor em ordem alfabética
print(max(lista_nomes)) #Aqui vai retornar o maior em ordem alfabética
"""








