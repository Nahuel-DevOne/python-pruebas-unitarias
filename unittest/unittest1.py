import unittest # librería que ya se encuentra en la biblioteca estandar de Python

class TestExample(unittest.TestCase):
    # el método debe ser siempre test_
    def test_suma_numeros(self):
        numero1 = 10
        numero2 = 20
    
        resultado = numero1 + numero2 #30
        
        self.assertEqual(resultado, 30)
    
    def test_resta_numeros(self):
        self.assertEqual(30-20, 10)
        
        
if __name__ == '__main__':
    unittest.main()
    
# para ejecutar la prueba: python unittest1.py
# para mayoro información: python unittest1.py -v