def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    t = ()
    for i in range(0, len(aTup), 2):
        t = t + (aTup[i],)
    return t
def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    n = 0
    for v in animals.values():
        n += len(v)
    return n
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    length = 0
    for v in aDict.values():
        if len(v) > length:
            length = len(v)
    for k, v in aDict.items():
        if len(v) == length:
            return k
