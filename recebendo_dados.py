"""
Recebendo dados do usuário
"""

print("Qual seu nome?")
name = input()
print("Qual sua idade?")
age = input()

#Forma antiga do Python (2.x)
#print("Seja bem vindo(a) %s" %name)
#print("Seja bem vindo(a) %s, com %s anos." %(name, age))

#Forma mais moderna do Python (3.x)
#print("Seja bem-vindo(a) {0}, com {1} anos.".format(name, age))

#Forma atual do Python
print(f'Seja bem-vindo(a){name}, com {age} anos.')