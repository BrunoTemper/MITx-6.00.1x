# Implement the function isIn(char, aStr) which uses bisection search
# to recursively test if char is in aStr. char will be a single character
# and aStr will be a string that is in alphabetical order.
# The function should return a boolean value.

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == '':
        return False

    if len(aStr) == 1:
        if char == aStr:
            return True
        else:
            return False

    guess = aStr[(len(aStr)/2)]

    if (guess == char):
        return True
    elif (guess > char):
         return isIn(char, aStr[:(len(aStr)/2)])
    elif (guess < char):
         return isIn(char, aStr[(len(aStr)/2):])
