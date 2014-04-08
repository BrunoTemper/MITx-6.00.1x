def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict

    Test Case:
    buildCoder(3) = {'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J', 'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O', 'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X', 'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'B', 'X': 'A', 'Z': 'C', 'a': 'd', 'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l', 'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q', 'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z', 'v': 'y', 'y': 'b', 'x': 'a', 'z': 'c'}
    
    """
    import string
    letters = string.ascii_uppercase + string.ascii_lowercase
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase

    # return object for Caesar cipher dictionary
    cipher = {}
    index = 0

    for l in letters:
        if (l in uppercase):
            if (shift + index > 51):
                cipher[l] = uppercase[shift+index-52]
            elif (shift+index > 25):
                cipher[l] = uppercase[shift+index-26]
            else:
                cipher[l] = uppercase[shift+index]
        elif (l in lowercase):
            if (shift + index > 51):
                cipher[l] = lowercase[shift+index-52]
            elif (shift+index > 25):
                cipher[l] = lowercase[shift+index-26]
            else:
                cipher[l] = lowercase[shift+index]
        index += 1

    return cipher
     

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text

    Test Cases:
    >>> applyCoder("Hello, world!", buildCoder(3))
    'Khoor, zruog!'
    >>> applyCoder("Khoor, zruog!", buildCoder(23))
    'Hello, world!'
    """
    ### TODO


def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.

    Test Case:
    >>> applyShift('This is a test.', 8)
    'Bpqa qa i bmab.'
    >>> applyShift('Bpqa qa i bmab.', 18)
    'This is a test.'
    
    """
    ### TODO.
    ### HINT: This is a wrapper function.
