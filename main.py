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
optimize = optimized_sets(optimize, unique_sets)
final_collection = new_key(optimize)

counter = 2
max_sets = N // 3
while max_sets > 0:
	if optimize[max(optimize)] == []:
		break
	optimize = optimized_sets(final_collection, unique_sets)	# Dictionary with key/value pairs that don't overlap
	final_collection = new_key(optimize)						# New dictionary with longer keys
	max_sets -= 1
	counter += 1

print(len(max(final_collection)) // 3)
print("")

# Part 3
sets = max(final_collection)
counter = 0
while counter != 3:
	if not sets:
		break
	print(sets[0])
	sets = sets[1:]
	if len(sets) % 3 == 0:
		print("")