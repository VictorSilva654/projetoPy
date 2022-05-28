"""
Testes Unitários com Python

os testes devem ser rodados no terminal, com python nome_do_modulo.py

para mais detalhes, podemos colocar python nome_do_modulo.py -v
"""

import unittest
from atividade import as_ideia_e_dura, cortar_giro
from nova_classe import Cantor

class AtividadeTeste(unittest.TestCase):
    # Para fazer uma classe de teste, ele deve herdar da classe TestCase do módulo UnitTest

    def setUp(self):
        #o Método SetUp é iniciado antes de iniciar os testes
        self.seu_jorge = Cantor("Seu Jorge")

    def test_cortar_giro_menos(self):
        self.assertEqual(
            cortar_giro(60),
            'A moto não é potente'
        ) #Aqui testa se os dois parâmetros são iguais, ou seja, se são true

    def test_cortar_giro_mais(self):
        self.assertEqual(
            cortar_giro(250),
            'RANDAMDANDANDAN'
        )

    def test_as_ideia_e_dura(self):
        self.assertTrue(as_ideia_e_dura(True))
        #Aqui testa se o parametro é True ou não

    def test_as_ideia_e_dura_false(self):
        self.assertFalse(as_ideia_e_dura(False))
        #Aqui testa se o parametro é False ou não

    def test_instancia(self):
        self.assertIsInstance(self.seu_jorge, Cantor)
        #Testando se o atributo é de uma classe ou não
    
    def test_nome(self):
        self.assertEqual(self.seu_jorge.nome, "Seu Jorge")
    
    
if __name__ == "__main__":
    unittest.main()