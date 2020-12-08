def closest_power(base, num):
    guess=0
    exp=1
    while abs(base**guess - num) != 0:
        if num > base**guess:
            if abs(base**guess - num) <= abs(base**exp - num):
                exp = guess
        if base**guess > num:
            if abs(base**guess - num) < abs(base**exp - num):
                exp = guess
            if abs(base**guess - num) > abs(base**exp - num):
                break
        guess += 1
    return exp


def dict_invert(dic):
    d = {}
    for v in dic.values():
        d[v] = []
    for k, v in dic.items():
        d[v].append(k)
        d[v].sort()
    return d


def max_val(t):
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """
    # Your code here

    def openItem(term):
        newList = []

        for item in term:
           if type(item) == int:
              newList.append(item)

           else:
              newList += openItem(item)

        return newList

    sortingList = openItem(t)

    maximum = sortingList[0]

    for item in sortingList:
        if maximum < item:
            maximum = item

    return maximum


def general_poly (L):
    """
    L: a list of numbers (n0, n1, n2, ... nk)
    Returns: a function, which when applied to a value x, returns the value
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0
    """
    def func(x):
        value = 0
        k = len(L) - 1
        for num in L:
            value = value + num * (x ** k)
            k -= 1
        return value
    return func