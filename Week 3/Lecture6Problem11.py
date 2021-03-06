def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    sum = None
    max = 0
    for k in aDict.keys():
        if len(aDict[k]) >= max:
            sum = k
            max = len(aDict[k])
    return sum
