class Bunny:
	def __init__(self, name):
		# Calling Bunny() now takes 1 parameter, name
		self.name = name

	def __str__(self):
		return self.name

def display_bunnies(bunnies):
	for bunny in bunnies:
	    print bunny

bunnies = []

names_of_bunnies = ['ted', 'fred', 'jenny']

for name in names_of_bunnies:
	bunnies.append(Bunny(name))

for bunny in bunnies:
	print bunny

names = []
filename = 'names.txt'
with open(filename, 'r') as f:
	for line in f:
	# This loops through the name.txt and adds each one to our list
	    names.append(line.strip()) 
	    '''we use strip to eliminate escape characters and 
	    white space, try it without strip to see the 
	    difference'''

# Creating 100 bunnies with a random name
import random

for _ in range(100):
    random_name = random.choice(names)
    bunnies.append(Bunny(random_name))

display_bunnies(bunnies)

with open('mybunnies.txt', 'w') as f:
    for bunny in bunnies:
        f.write(str(bunny) + '\n')
        # We can only write strings to a file so we include str()
