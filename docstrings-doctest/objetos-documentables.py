"""Este es el Docstring del módulo objetos-documentables."""
# El docstring debe encontrarse en la primera línea del bloque
# Importante, utilizar con nombre main

# objetos documentables:
# A todos aquellos objetos que se puedan documentar con docstrings
# Poseen el atributo __doc__
# - funciones
# - clases
# - métodos
# - módulos

class user:
    """Permite representar un usuario."""
    def __init__(self, username: str, password: str) -> None:
        """Permite instanciar un objeto de tipo User

        Args:
            username (str): El username del usuario
            password (str): El password del usuario
        """

def palindromo(sentence: str) -> bool:
    """Permite conocer si un string es o no un palíndromo.

    Args:
        sentence (str): string a evaluar

    Returns:
        bool: True o False
    
    Examples:
    
    >>> palindromo('Anita lava la tina')
    True
    
    >>> palindromo('CodigoFacilito')
    False
    
    >>> sentence = 'Oso'
    >>> palindromo(sentence)
    True
    """
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]


palindromo('Anita lava la tina')