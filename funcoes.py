"""
Criando funções em python

#Função sem parâmetro e sem retorno 
def salve():
    print("Salve!")

salve()

#Função com retorno
def soma_de_2_mais_2():
    return 2+2

print(soma_de_2_mais_2())

#Função com parâmetro
def soma_simples(valor1, valor2):
    return valor1 + valor2

v1 = int(input("Coloque um valor aqui: "))
v2 = int(input("Coloque outro valor: "))

print(soma_simples(v1, v2))


#Função com parâmetro padrão, ou seja, aquela que quando chamada, não precisa ser setado um valor
def exponencial(numero, potencia=2):
    return numero ** potencia

print(exponencial(2))
print(exponencial(2, 6))

"""

