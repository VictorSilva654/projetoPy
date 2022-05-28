"""
Iteradores e iteráveis

Iteradores ou iterators, são objetos que podem ser iterados Ele retorna um dado 
quando a função next() é chamada. EX: Um generator

Iteráveis são objetos que retornam um iterador quando a função iter() é chamada. EX: Listas, strings, etc.

def conte_ate(num_max):
    contador = 1
    while contador <= num_max:
        yield contador
        contador = contador + 1

gerador = conte_ate(5)

print(gerador)
"""

#Criando generator funcions (funções geradoras). Elas retornam um generator e usam a palavra yield.

