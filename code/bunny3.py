class Bunny:
	def __init__(self, name, weight):
		# Calling Bunny() now takes 2 parameters
		self.name = name
		self.weight = weight

	def __str__(self):
		return self.name

def display_bunnies(bunnies):
	for bunny in bunnies:
		# bunny and bunny.name will give us same results but this is how we access attributes
		# spacing is more my OCD so bunny.weights are in a column
		spacing = 20
		print bunny.name + ' '*(spacing - len(bunny.name)) + str(bunny.weight)

bunnies = []

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
    random_number = random.randrange(1,11) # selects a random number between 1-10
    bunnies.append(Bunny(random_name, random_number))

display_bunnies(bunnies)

with open('mybunnies.txt', 'w') as f:
    for bunny in bunnies:
        f.write(str(bunny.name) + ' | ' + str(bunny.weight) + '\n')
        # We can only write strings to a file so we include str()


'''
In this post, we will modify our code in `class Bunny` to include other attributes. An attribute belong to a class object.
Our imaginary friends have an age, weight, name, and other attributes. Let's practice adding in a new attribute together.

{% highlight python %}
class Bunny:
	def __init__(self, name, weight):
		# Calling Bunny() now takes 2 parameters
		self.name = name
		self.weight = weight

{% endhighlight %}

Now, let's edit our code to add in the new parameter `weight` into our code. 
We will make use of the built-in python method `random.randrange()` to make our imginary friends weights different without 
hard-coding everything. 

{% highlight python %}

import random

for _ in range(100):
    random_name = random.choice(names)
    random_number = random.randrange(1,11) # selects a random number between 1-10
    bunnies.append(Bunny(random_name, random_number))

{% endhighlight %}

Let's also take some time to update our `display_bunnies` function so we can visually see the different weights.

{% highlight python %}

def display_bunnies(bunnies):
	for bunny in bunnies:
		# bunny and bunny.name will give us same results but this is how we access attributes
		# spacing is more my OCD so bunny.weights are in a column
		spacing = 20
		print bunny.name + ' '*(spacing - len(bunny.name)) + str(bunny.weight)

{% endhighlight %}

Our imaginary bunnies now have names and weights! We will need to also update the code that writes to our file, `mybunnies.txt` to include weights. 
We need to make sure we convert the `bunny.weight` into a string using `str()`.

{% highlight python %}
f.write(str(bunny.name) + ' | ' + str(bunny.weight) + '\n')
{% endhighlight %}

There are a lot of potentional attributes we can add for our bunnies depending on how creative you want to be. 
We can add gender, breeds, and attributes like `alive=True` using `boolean variables`. 
{% highlight python %}

{% endhighlight %}

{% highlight python %}

{% endhighlight %}

{% highlight python %}

{% endhighlight %}

'''