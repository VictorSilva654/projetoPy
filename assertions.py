"""
Assertions é um tipo de verificação de código
"""

def lista_de_compras(item):
    assert item in [
        "Laranja",
        "Bom-bril",
        "Detergente",
        "Carne",
        "Arroz",
        "Cheiro Verde"
    ], "O item não está na lista de compras"

lista_de_compras("Bom-bril")
#lista_de_compras("Sorvete") #Aqui sai um erro

