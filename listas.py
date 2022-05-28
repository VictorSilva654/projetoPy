"""
Apendendo listas em Python
"""

lista1 = [1, 2, 6, 76, 350, 24, 86, 190, 66, 274, 26]
print(lista1)

"""
#lista1.sort() organiza a lista em ordem crescente

soma = 0 #Iterando sobre as listas
for elemento in (lista1):
    print(elemento)
    soma = soma + elemento
print(soma)

lista2 = lista1.copy() #copiando a lista
print(lista2)

lista1.append(54) #colocando um valor na lista. OBS: o append só aceita um valor
lista1.append([65, 34, 64]) 
#aqui colocamos uma lista no append, mas ele entendeu como apenas um valor, que é a lista
print(lista1)
lista1.extend([66, 74, 21]) 
#para colocar mais de um valor na lista, utilizamos o extend, porém temos que colocar como uma lista
print(lista1)

print(len(lista1)) #Imprime o tamanho (length) da lista

lista1.pop()
#o pop tira o valor da lista, como não especificamos o índice, ele tirou o último
lista1.pop(6)
#agora vai tirar o valor da lista no índice 6
print(lista1) 
"""

