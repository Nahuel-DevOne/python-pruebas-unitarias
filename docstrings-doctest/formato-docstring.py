# Docstring: es un comentario
# Donde se va a almacenar la información de la documentación:
# __doc__

def palindromo(sentence: str) -> bool:
    # Docstring con el estilo de Google
    # se hace con """ + tab o ''' + tab y lo genera
    """_summary_

    Args:
        sentence (str): _description_

    Returns:
        bool: _description_
    """
    
    # reemplazando como debiera quedar
    """Permite conocer si un string es o no un palíndromo.

    Args:
        sentence (str): string a evaluar

    Returns:
        bool: True o False
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