def func_m(x):
    """

    >>> func_m(2)
    32

    >>> func_m(3)
    145
    
    """
    return round (pow(x,4)+pow(4,x))
import doctest
#роверяет тесты в доках
doctest.testmod()
