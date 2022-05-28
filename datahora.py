"""
Data e Hora em Python

nascimento = input("Insira sua data de nascimento: ")
nascimento = nascimento.split('/')

nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)

"""

import datetime

datahora = datetime.datetime.now()

print(datahora)

datahora_nova = datetime.datetime(2023, 11, 30, 19, 35)

print(datahora_nova)

data_delta = datahora_nova - datahora

print(data_delta)

delta_formatado = datahora.strftime('%d/%m/%Y')

print(delta_formatado)