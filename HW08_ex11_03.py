#!/usr/bin/env python
# Exercise 3  
# Dictionaries have a method called keys that returns the keys of the 
# dictionary, in no particular order, as a list.

# (1) Modify print_hist_old to print the keys and their values in alphabetical 
# order.

# (2) Paste in your completed functions from HW08_ex_11_02.py

# (3) Within main() make the appropriate function calls to print the
# alphabetical histogram of pledge.txt
##############################################################################
import re

def print_hist_old(h):
    for key in sorted(h.keys()):
		print key, h[key]

def print_hist_new(h):
    print print_hist_old(h)


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
##############################################################################
def main():
	""" Calls print_hist_new with the appropriate arguments to print the 
    histogram of pledge.txt.
    """
	pledge_histogram = histogram_new(get_pledge_list())
	print_hist_new(pledge_histogram)
	

if __name__ == '__main__':
    main()
