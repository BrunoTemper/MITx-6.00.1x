def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    guess = min(a,b)
    while (guess > 0):
        if (a % guess == 0) and (b % guess == 0):
            return guess
        elif (guess == 1):
            return 1
        guess -= 1
        
        
    
