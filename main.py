# File split into two parts. Part 1 will import a file and streamline the input to give 
# a variable N, and an array of all the cards given. Also, this part will assert that the
# conditions from the specification are true. Part 2 takes the N and array of cards from part 1
# and will print the number of SETs, Disjoint SETS, and the collection of disjoint SETs to the
# Terminal.

from sets import *
from utils import *
import random

################
# Import Stdin #
################
import fileinput

cards = []
for line in fileinput.input():
	cards += [line.replace("\n", "")]

N = int(cards[0])

while "" in cards:
	cards.remove("")

cards.pop(0)

assert 3 <= N <= 30, 'Int N is not within proper range.'
assert len(cards) == N, 'Int N does not match number of cards provided.'



###################################
# Sets, Disjoint Sets, Collection #
###################################

# Part 1
all_subsets = subsets(cards, 3)										# All subsets of size 3 possible with given cards
valid_sets = [cards for cards in all_subsets if valid_set(cards)]	# All valid SETS found in subsets
print(len(valid_sets))

# Part 2
set_pairs = subsets(valid_sets, 3)
all_disjoint_sets = [set_pair for set_pair in set_pairs if disjoint_set(set_pair)]
unique_sets = set([tuple(myset) for myset in flatten(all_disjoint_sets[:])])

random_card = random.choice(flatten(list(unique_sets)))
optimize = {sets:[] for sets in unique_sets if random_card in sets}
for key in optimize:
	unique_sets.remove(key)

for key, value in optimize.items():
	for card_set in unique_sets:
		if key[0] not in card_set and key[1] not in card_set and key[2] not in card_set:
			value += [card_set]






