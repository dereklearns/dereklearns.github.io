---
layout: post
title:  "Attributes and Bunnies"
date:   2019-05-6 07:10:34 -0500
categories: python read write I\O classes attributes
---

# Attributes
In this post, we will modify our code in `class Bunny` to include attributes. An attribute belongs to a class object.
Our imaginary bunny friends can have several attributes like...age, weight, anda name. Let's practice adding in a new attribute together.

{% highlight python %}
class Bunny:
	def __init__(self, name, weight):
		# Calling Bunny() now takes 2 parameters
		self.name = name
		self.weight = weight

{% endhighlight %}

Now, let's edit our code that creates bunnies to take the new parameter `weight`. 
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

Our imaginary bunnies now have names and weights! 
Let's update our function that writes to our file, `mybunnies.txt` to include the weights. 

We need to make sure we convert the `bunny.weight` into a string using `str()`.

{% highlight python %}
f.write(str(bunny.name) + ' | ' + str(bunny.weight) + '\n')
{% endhighlight %}

Think of the possible attributes we can add for our bunnies. We can add gender, breeds, and attributes like `alive=True` using `boolean variables`. Try adding a few more attributes on your own, make sure to update the the parameters in the `__init__` and `Bunny(name, weight, ...)`
