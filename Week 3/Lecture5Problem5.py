def gcdRecur(a, b):
    '''
    a, b: positive integers
    Using Euclid's algorithm for greatest common divisor:
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if (b == 0):
        return a
    else:
        return gcdRecur(b, a % b)
    
