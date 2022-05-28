"""
Leitura de arquivos em Python

#Abrindo o texto
salve = open('salve.txt')

#Trabalhando com o texto todo
print(salve.read())

#Fechando o texto
salve.close()

"""


#Forma certa de trabalhar com arquivos
with open("salve.txt") as arquivo:
    print(arquivo.read())