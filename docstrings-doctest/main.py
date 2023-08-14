"""Este es el Docstring del módulo main"""

class User:
    """Permite representar un usuario."""
    
    def __init__(self, username: str, password: str) -> None:
        """Permite instanciar un objeto de tipo User

        Args:
            username (str): El username del usuario
            password (str): El password del usuario
        """
        
        self.username = username
        self.password = password
        

def palindromo(sentence: str) -> bool:
    """Permite conocer si un string es o no un palíndromo.

    Args:
        sentence (str): string a evaluar

    Returns:
        bool: True o False
    """
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]

palindromo('Anita lava la tina')

##### Las casos de prueba se corrieron a test_main.txt
# Para ejecutarlos, desde el directorio docstrings-doctest:
# python -m doctest test_main.txt

# Para ver la prueba:
# python -m doctest test_main.txt - v
