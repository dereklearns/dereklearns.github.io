---
layout: post
title:  "Exploring the use of Classes and Object Oriented Programming using Python"
date:   2019-04-26 05:18:34 -0500
categories: python classes oop 
---
# Classes

One of the most difficult programming concepts for new programmers ot understand is `classes`. I hope to help you understand how `classes` work through the use of imaginary bunnies in the examples below.

You can reference the python documentation on `classes` [here](https://docs.python.org/3/tutorial/classes.html)


# Creating a class
Below we will create a new `class` named `Bunny`. In Python, we need to write the `__init__` method which runs when a `class` object is created. 

{% highlight python %}
class Bunny:
	def __init__(self):
		pass

mybunny = Bunny()
# storing a Bunny object in the variable 'mybunny'

{% endhighlight %}

Congrats, you created your first object in Python using the Bunny class. 

Try running `print(mybunny)`.
You will see results similiar to:
> <__main__.Bunny instance at ~~0x7f7201ece680>~~

This is saying, that you variable mybunny is a Bunny object/instance and it lists a memory address. What if we had a bunch of Bunnies, how could we tell the difference between them?

{% highlight python %}
class Bunny:
	def __init__(self):
		pass

mybunny1 = Bunny()
mybunny2 = Bunny()
mybunny3 = Bunny()

print(mybunny1)
print(mybunny2)
print(mybunny3)

{% endhighlight %}

The results I got were:
> <__main__.Bunny instance at 0x7f36b25b0680><br>
> <__main__.Bunny instance at 0x7f36b25b06c8><br>
> <__main__.Bunny instance at 0x7f36b25b0710>

Do you see the difference? We know they are different but, this is not ideal.

Let's try giving each Bunny a name.

{% highlight python %}
class Bunny:
	def __init__(self, name):
		# Calling Bunny() now takes 1 parameter, name
		self.name = name

mybunny1 = Bunny('ted')
mybunny2 = Bunny('fred')
mybunny3 = Bunny('jenny')
# each buny now has a name under their attribute name
print(mybunny1.name)
print(mybunny2.name)
print(mybunny3.name)

{% endhighlight %}

Running this code should give us each Bunnies name, but this is still not ideal. There is a better way using the `__str__` method.

{% highlight python %}
class Bunny:
	def __init__(self, name):
		# Calling Bunny() now takes 1 parameter, name
		self.name = name
		
	def __str__(self):
		# This will replace the <main.Bunny instance at
		# 0x7f36b25b0680> with the Bunnies name
		return self.name

# Let's also refactor this code to make it easier to test
bunnies = []

names_of_bunnies = ['ted', 'fred', 'jenny']

for name in names_of_bunnies:
	bunnies.append(Bunny(name))

for bunny in bunnies:
	print(bunny)

{% endhighlight %}

Now that our code is refactored, we can create LOTS of bunnies. Go ahead and try to make a bigger list of names and give it a try.

We will continue to learn more about classes with our imaginary bunnies in the next post.



