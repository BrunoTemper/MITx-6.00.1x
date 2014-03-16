def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    sum = 0
    for value in aDict.values():
        sum += len(value)
    return sum
