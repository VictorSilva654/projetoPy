"""
Trabalhando com CSV 
"""

from csv import reader

with open("lutadores.csv") as arquivo:
    leitor_csv = reader(arquivo)
    for linha in leitor_csv:
        print (f"O lutador {linha[0]} é do país {linha[1]} e tem{linha[2]}")