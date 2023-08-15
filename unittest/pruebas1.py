# assert

if __name__ == '__main__':
    try:
        assert 5 == 10, 'Lo sentimos cinco no es igual a diez.'
        # otra forma de hacerlo, pero no es código pythonico, se prefiere el assert
        # if not 5 == 10:
        #     raise AssertionError('Lo sentimos cinco no es igual a diez.')
        
        print('>>> El programa continua con su ejecución')
    
    except AssertionError as error:
        print(error)
        
        
