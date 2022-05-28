"""
Decoradores (Decorators)

São incrementos que podemos dar à função. Podemos chamá-los com @

Decoration Functions são funções que podem acresentar o funcionamento de outras funções.
"""

#Exemplo:

def cumprimento(funcao):
    funcao()
    return "To aqui hein"


@cumprimento
def me_de_salve():
    print("Salve!")

print(f"{me_de_salve}")