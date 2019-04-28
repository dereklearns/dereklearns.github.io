class Bunny:
	def __init__(self, name):
		# Calling Bunny() now takes 1 parameter, name
		self.name = name

	def __str__(self):
		return self.name

bunnies = []

names_of_bunnies = ['ted', 'fred', 'jenny']

for name in names_of_bunnies:
	bunnies.append(Bunny(name))

for bunny in bunnies:
	print bunny
