class Coordinate(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self, other):
        return self.x == other.getX() and self.y == other.getY()

    def __repr__(self):
        return 'Coordinate(' + str(self.x) + ',' + str(self.y) + ')'

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def intersect(self, s2):
        s = intSet()
        for i in self.vals:
            if i in s2.vals:
              s.insert(i)
        return s

    def __len__(self):
        return len(self.vals)


    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
#
#
# class Accio(Spell):
#     def __init__(self):
#         Spell.__init__(self, 'Accio', 'Summoning Charm ')
#
#     def __str__(self):
#         return self.incantation + self.name + '\n This charm summons an object to the caster, potentially over a significant distance.'()

# def genPrimes():
#     x = 0
#     flag = False
#     while x < 10:
#         for i in range (1, 10):
#             if x % i == 0:
#                 flag = True
#         if flag == False:
#             yield x
#         flag = False
#         x += 1

def genPrimes():
    primeList = [2]
    x = 3
    yield 2
    while True:
        flag = 0
        for p in primeList:
            if x % p == 0:
                flag = 1
                break
        if flag == 0:
            yield x
            primeList.append(x)
        x += 1