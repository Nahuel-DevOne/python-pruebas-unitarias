def suma_numeros_positivos(n1:int, n2:int) -> int:
    """Permite sumar dos números enteros positivos

    Args:
        n1 (int): _description_
        n2 (int): _description_

    Returns:
        int: _description_
    """
    # if n1 < 0 or n2 < 0:
    #     return None
    
    # Delegamos la responsabilidad de manejar el error a quien llamó la función.
    assert n1 > 0 and n2 > 0, 'Lo sentimos solo es posible sumar números positivos'
    
    return n1 + n2

if __name__ == '__main__':
    resultado = suma_numeros_positivos(-10,20)
    print(resultado)
    
