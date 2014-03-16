# Write an iterative function, lenIter, which computes the length
# of an input argument (a string), by counting up the number of
# characters in the string.

def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    length = 0
    if aStr == '':
        return 0
    while (aStr[length:] != ''):
        length += 1
    return length
