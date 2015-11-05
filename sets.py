# File where I will be keeping all functions operating on array of cards
# to produce final collections and sets.

from utils import *
from random import shuffle
from functools import reduce

def valid_set(subset):
	""" Takes in a set of 3 cards and returns a list of of lists where 
	every sublist is the list of a certain attribute across all cards.
	Then compares the attributes to see if they are all the same or are
	all different.

	"""
	colors = [get_color(card) for card in subset]
	symbols = [get_symbol(card) for card in subset]
	shades = [get_shade(card) for card in subset]
	numbers = [get_number(card) for card in subset]
	return (all_same(colors) or all_different(colors)) and (all_same(symbols) or all_different(symbols)) and (all_same(shades) or all_different(shades)) and (all_same(numbers) or all_different(numbers))

def disjoint_set(set_trio):
	""" All possible disjoint sets, where no card can be included in 
	any pair of cards, not accounting for the card being repeated in
	other disjoint sets.

	"""
	all_sets = subsets(set_trio, 2)
	for pair in all_sets:
		set1, set2 = pair[0], pair[1]
		for card in set1:
			if card in set2:
				return False
	return True

def flatten(lst):
	""" Takes a list of list and flattens it into a single list with no
	deep lists.

	"""
	return [inner_list for sublist in lst for inner_list in sublist]

def all_cards(disjoint):
	""" Function that gives me all unique cards left when making disjoint
	sets.

	"""
	#flat_disjoints = [flatten(sets) for sets in disjoint]
	used_cards = []
	for subset in disjoint:
		for card in subset:
			if card not in used_cards:
				used_cards += [card]		
	return used_cards



