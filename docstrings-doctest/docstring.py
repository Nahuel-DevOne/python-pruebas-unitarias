# Docstring: es un comentario
# Donde se va a almacenar la información de la documentación:
# __doc__

def palindromo(sentence: str) -> bool:
    """ Permite conocer si un string es o no un palíndromo.
    
    Args:
        sentence: string
    Returns:
        bool
    """
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]


palindromo('Anita lava la tina')

# en la terminal, parado desde el directorio de docstring, ejecutar Python: 
# palindromo('Anita Lava la Tina')
# True

# Para ver la documentación en la terminal:
# palindromo.__doc__
# help(palindromo)