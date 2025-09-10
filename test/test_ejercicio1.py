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
        self.assertIsNone(definir_precio(80),25000)
    def test_edad_invalida_negativos(self):
        self.assertIsNone(definir_precio(-5))
        self.assertIsNone(definir_precio(-10))
    def test_fuera_de_rango(self):
        self.assertIsNone(definir_precio(100))
if __name__ == '__main__':
    unittest.main()