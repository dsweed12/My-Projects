import math


def iter_power(base, exp):
    """
    base: int or float
    exp: int >= 0

    returns: int or float, base^exp
    """
    if exp == 0:
        return 1
    else:
        result = base
    while exp > 1:
        result *= base
        exp -= 1
    return base


def recurPower(base, exp):
    """
    base: int or float
    exp: int >= 0

    returns: int or float, base^exp
    """
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * recurPower(base, exp-1)


# Exercise 1:
iteration = 0
while iteration < 5:
    count = 0
    for letter in "hello, world":
        count += 1
        if iteration % 2 == 0:
            break
    print("Iteration " + str(iteration) + "; count is: " + str(count))
    iteration += 1
# exercise 2:
x = 25
epsilon = 0.01
step = 0.1
guess = 0.0

while abs(guess**2-x) >= epsilon:
    if guess <= x:
        guess += step
    else:
        break

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))

#guess any number:
print("Please think of a number between 0 and 100")
low, high = 0, 100
mid = int((high +low)/2)
print("is your secret number "+ str(mid) +"?")
ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
while ans != "":
    if ans == 'c':
        break
    elif ans =='h':
        high = mid
    elif ans == 'l':
        low = mid
    else:
        print("Sorry, I did not understand your input.")
    mid = int((low + high)/2)
    print("is your secret number " + str(mid) + "?")
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
print("Game over. Your secret number was:" + str(mid))

def printMove(fr, to, tree):
    print("Tree "+str(tree)+": Move from "+str(fr)+" to "+str(to))


def towers(n, fr, to, spare, tree):
    if n == 1:
        printMove(fr, to, tree)
    else:
        towers(n-1, fr, spare, to, 1)
        towers(1, fr, to, spare,2)
        towers(n-1, spare, to, fr,3)



def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    guess = min(a, b)
    while a % guess > 0 or b % guess > 0:
        guess -= 1
    return guess


def gcdRecur(a, b):
    """
     a, b: positive integers
     returns: a positive integer, the greatest common divisor of a & b.
    """
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)


def isIn(char, aStr):
    """"
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    """
    found = False
    if aStr == "":
        return False
    else:
        if aStr[0] == char or aStr[-1] == char:
            return True
        mid = aStr[len(aStr)//2]
        if mid == char:
            return True
        elif mid > char:
            return isIn(char, aStr[0:len(aStr)//2-1])
        else:
            return isIn(char, aStr[len(aStr) // 2:-1])


def polysum(n, s):
    import math
    area = (.25*n*s**2)/math.tan(math.pi/n)
    perimeter = n*s
    sum = area+perimeter**2
    return round(sum, 4)