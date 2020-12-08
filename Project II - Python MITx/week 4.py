def integerDivision(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the integer division of x divided by a.
    """
    count = 0
    while x >= a:
        count += 1
        x = x - a
    return count


def rem(x, a):
    """
    x: a non-negative integer argument
    a: a positive integer argument

    returns: integer, the remainder when x is divided by a.
    """
    if x == a:
        return 0
    elif x < a:
        return x
    else:
        rem(x-a, a)


def fancy_divide(list_of_numbers, index):
    try:
        denom = list_of_numbers[index]
        return [simple_divide(item, denom) for item in list_of_numbers]
    except ZeroDivisionError:
        l =[]
        for n in list_of_numbers:
            l.append(0)
        return l


def simple_divide(item, denom):
    return item / denom
