import unittest
from ejercicio_1 import definir_precio
class TestEjercicio1(unittest.TestCase):
    def test_definir_edad_niño(self):
        self.assertEqual(definir_precio(10),10000)
    def test_definir_edad_adolescente(self):
        self.assertEqual(definir_precio(15),15000)
    def test_definir_edad_adulto(self):
        self.assertEqual(definir_precio(30),20000)
    def test_definir_superedad(self):
        self.assertIsNone(definir_precio(80))
    def test_edad_invalida(self):
        self.assertIsNone(definir_precio(-5))
    def test_negatios(self):
        self.assertEqual(definir_precio(-10),-10)
if __name__ == '__main__':
    unittest.main()