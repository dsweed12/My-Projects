def sum_digits(s):
	""" assumes s a string
	    Returns an int that is the sum of all of the digits in s.
	      If there are no digits in s it raises a ValueError exception. """
	flag = False
	sum = 0
	while i <= len(s) - 1:
		try:
			n = int(s[i])
			sum += n
			flag = True
		except ValueError:
			i += 1
	if i == len(s) - 1 and flag == False:
			raise ValueError
	return sum

def sum_digits2(s):
	""" assumes s a string
		    Returns an int that is the sum of all of the digits in s.
		      If there are no digits in s it raises a ValueError exception.
		      """
	l = [x for x in s if x.isdigit()]
	if l == []:
		raise ValueError
	else:
		sum = 0
		for n in l:
			sum += int(n)
		return sum

def is_list_permutation(L1, L2):
	'''
	L1 and L2: lists containing integers and strings
	Returns False if L1 and L2 are not permutations of each other.
			If they are permutations of each other, returns a
			tuple of 3 items in this order:
			the element occurring most, how many times it occurs, and its type
	'''
	if L1 == [] and L2 == []:
		return (None, None, None)
	freq = {}
	for item in L1:
		if item in freq:
			freq[item] += 1
		else:
			freq[item] = 1
	frq = freq.copy()
	for item in L2:
		if item in freq:
			frq[item] -= 1
	frq = {x:y for x, y in frq.items() if y != 0}
	if frq == {} and freq.values() != []:
		try:
			mostTimes = max(freq.values())
			for k, v in freq.items():
				if v == mostTimes:
					mostTimesElement = k
					break
			mostTimesType = type(mostTimesElement)
		except ValueError:
			return False
		if len(L1) == len(L2):
			return (mostTimesElement, mostTimes, mostTimesType)
		else:
			return False

	else:
		return False


def dict_interdiff(d1, d2):
	'''
	d1, d2: dicts whose keys and values are integers
	Returns a tuple of dictionaries according to the instructions above
	'''
	intersection = {}
	difference = {}
	for k, v in d1.items():
		if k in d2.keys():
			intersection[k] = f(v, d2[k])
		else:
			difference[k] = v
	for k2, v2 in d2.items():
		if k2 not in d1.keys():
			difference[k2] = v2
	return (intersection, difference)