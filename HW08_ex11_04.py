#!/usr/bin/env python
# Exercise 4  
# (1) Modify reverse_lookup_old so that it builds and returns a list of all
# keys that map to v, or an empty list if there are none.

# (2) Paste in your completed functions from HW08_ex_11_02.py

# (3) Do not edit what is in main(). It should print what is returned, a list
# of the keys that map to the values passed.
##############################################################################
import re

def reverse_lookup_old(d, v):
	new_list = []
	for k in d:
		if d[k] == v:
			if d[k] in new_list:	
				continue
			else:
				new_list.append(k)
	return new_list
		

def reverse_lookup_new(d, v):
	return reverse_lookup_old(histogram_new(get_pledge_list()),v)
	


##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 BELOW: ##################
##############################################################################
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

##############################################################################
################### INSERT COMPLETED CODE FROM 11_02 ABOVE: ##################
##############################################################################
def main():   # DO NOT CHANGE BELOW
	pledge_histogram = histogram_new(get_pledge_list())
	print pledge_histogram
	print reverse_lookup_new(pledge_histogram, 1)
	print reverse_lookup_new(pledge_histogram, 9)
	print reverse_lookup_new(pledge_histogram, "Python")

if __name__ == '__main__':
    main()
