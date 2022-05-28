"""
Tratamento de erros

#Try/Except
def mostrar_dicionario(dicionario, chave):
    try:
        return dicionario[chave]
    except TypeError as errType:
        return f"Retornou o seguinte erro: {errType}"
    except KeyError as errKey:
        return f"Você adicionou uma chave errada"

dic = {'chave1': "valor1"}

print(mostrar_dicionario(dic, "chave1")) #Execução certa
print(mostrar_dicionario(6, "chave1")) #TypeError
print(mostrar_dicionario(dic, "y")) #KeyError

#Try/Except/Else/Finally

def calculo_simples():
    try:
        valor1 = int(input("Insira o primeiro valor: "))
        valor2 = int(input("Insira o segundo valor: "))
    except ValueError as err:
        print(f"Ocorreu um erro: {err}")
    else:
        print(valor1 + valor2)
    finally:
        print("Terminou o código!")

calculo_simples()

"""






