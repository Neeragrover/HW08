#!/usr/bin/env python
# Exercise 2  
# Dictionaries have a method called get that takes a key and a default value.
# If the key appears in the dictionary, get returns the corresponding value; 
# otherwise it returns the default value. For example:

# >>> h = histogram('a')
# >>> print h
# {'a': 1}
# >>> h.get('a', 0)
# 1
# >>> h.get('b', 0)
# 0

# (1) Use get to write histogram_old more concisely. You should be able to
# eliminate the if statement.

# (2) Use histogram_new to take pledge.txt and create a dict histogram with
# word counts (do not change the case of the words).
##############################################################################

# Imports
import re

# Body
def histogram_old(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def histogram_new(s):
	d = dict()
	for c in s:
		d[c] = d.get(c,0)
		d[c] +=1
	return d

def get_pledge_list():
	""" Opens pledge.txt and converts to a list, each item is a word in 
    the order it appears in the original file. returns the list.
    """
	with open("pledge.txt") as f:
		data = f.read()
	data1 = re.sub('[\W]+', ' ',data)
	x = data1.split()
	return x

	
    # Your code here.

    #return pledge_list (uncomment this)

##############################################################################
def main():  # DO NOT CHANGE BELOW
#	print "old histogram"
#	print histogram_old({'a':1,'b':2,'c':3})
#	print histogram_old("hello")
#	print " new histogram"
#	print histogram_new("hello	")
#	get_pledge_list()
	print histogram_new(get_pledge_list())

if __name__ == '__main__':
    main()
