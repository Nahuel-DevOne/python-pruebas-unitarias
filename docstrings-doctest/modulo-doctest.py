# Docstring: es un comentario
# Donde se va a almacenar la información de la documentación:
# __doc__

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

# Ejecutar en la terminal desde el directorio docstrings-doctest:
# python -m doctest modulo-doctest.py
# Si no se obtiene ningún tipo de salida, es porque todas las sentencias se ejecutaron correctamente
# Si no se cumple correctamente, se lanzará una excepción (error).

# Para más información:
# python -m doctest modulo-doctest.py -v
# Este si retorna un resultado mostrando el test se cumpla o no.