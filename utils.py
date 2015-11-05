# Collection of standard functions that may be useful in sets

#############
# Selectors #
#############
def get_color(card):
	colors = ["blue", "green", "yellow"]
	for color in colors:
		if color in card:
			return color

def get_symbol(card):
	symbols = {'H': ['h', 'H', '#'], 'S': ['s', 'S', '$'], 'A': ['a', 'A', '@']}
	symbol = card[len(card) - 1]
	for key, value in symbols.items():
		if symbol in value:
			return key

def get_shade(card):
	all_shades = {'lower': ['a', 's', 'h'], 'upper': ['A', 'S', 'H'], 'symbol': ['@', '$', '#']}
	shade = card[len(card) - 1]
	for key, value in all_shades.items():
		if shade in value:
			return key

def get_number(card):
	return card.count(card[len(card) - 1])

####################
# Helper Functions #
####################
def all_different(attributes):
	""" Helper function return True if all elements in a list are
	different, otherwise it returns False.

	>>> all_different(['blue', 'green', 'yellow'])
	True
	>>> all_different(['H', 'S', 'A'])
	True
	>>> all_different(['#', '$', '@'])
	True
	>>> all_different(['s', 'h', 'a'])
	True
	>>> all_different([1, 2, 3])
	True
	"""
	equality = [not (attributes[0] == attributes[1]), not (attributes[0] == attributes[2]), not (attributes[1] == attributes[2])]
	return all(equality)

def all_same(attributes):
	""" Return True if every element in lst if the same. Otherwise, 
	return False.

	>>> all_same(['blue', 'blue', 'blue'])
	True
	>>> all_same([3, 3, 3])
	True
	>>> all_same(['@', '@', '@'])
	True
	>>> all_same(['a', 'a', 'a'])
	True
	>>> all_same(['H', 'H', 'H'])
	True
	"""
	return attributes[0] == attributes[1] and attributes[0] == attributes[2] and attributes[1] == attributes[2]

def subsets(lst, n):
	""" Return a list of all subsets of size n, using elements from 
	the initial lst. 

	"""
	if n == 0:
		return [[]]
	if len(lst) == n:
		return [lst]
	return [[lst[0]] + x for x in subsets(lst[1:], n - 1)] + subsets(lst[1:], n)


def optimized_sets(dictionary, unique_sets):
	""" Function that will iterate over all unique sets we have
	and map them to a dictionary where the key is a tuple of cards
	that aren't included in our current sets
	"""
	for sets in unique_sets:
		for keys in dictionary:
			if (sets[0] not in keys) and (sets[1] not in keys) and (sets[2] not in keys):
				dictionary[keys] += [sets]
	return dictionary

def optimized_sets2(dictionary, current):
	""" Function that will iterate over all unique sets we have
	and map them to a dictionary where the key is a tuple of cards
	that aren't included in our current sets
	"""
	for key in dictionary:
		for keys, values in current.items():
			if (values[0] not in key) and (values[1] not in key) and (values[2] not in key):
				dictionary[key] += values
	return dictionary

def new_key(dictionary):
	new_dictionary = {}
	for key, value in dictionary.items():
		for sets in value:
			if sets:
				new_dictionary[key + sets] = []
			elif value == []:
				dictionary[key] = value
	return new_dictionary

def delete(dictionary, num):
	keys_to_delete = [key for key in dictionary if len(key) < num or dictionary[key] == []]
	for key in keys_to_delete:
		del dictionary[key]
