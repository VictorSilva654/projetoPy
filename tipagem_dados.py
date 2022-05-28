"""
Especificando dados
"""

#com as novas atualizações do Python, conseguimos especificar os tipos da função
def ola_amigo(amigo: str) -> str:
    return f"Olá {amigo}"

print(ola_amigo("Denilson"))