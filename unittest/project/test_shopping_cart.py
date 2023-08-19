import unittest
from product import Product

class TestShoppingCart(unittest.TestCase):
    
    def test_product_object(self):
        name = 'Manzana'
        price = 1.70
        
        product = Product(name, price)
        
        # assert product.name == name, 'error: el nombre no es el mismo' 
        # assert product.price == price, 'error: el precio no es el mismo'
        
        self.assertEqual(product.name, name, 'error: el nombre no es el mismo')
        self.assertEqual(product.price, price, 'error: el precio no es el mismo')
        

if __name__ == '__main__':
    unittest.main()
    
# para correr la prueba en la terminal:
# python test_shopping_cart.py    
    
    
    