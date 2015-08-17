import sys
import random

def get_num_of_digits():
	"""This function checks if the user provided the number if digits at the command line. If not, it prompts the user to enter it.
	It finally returns the user entered value"""
	if len(sys.argv) == 1:
		num_of_digits = raw_input("Please enter the number of digits: ")
	else:
		num_of_digits = sys.argv[1]
	return num_of_digits
	
def check_for_num(number):
	""" This function checks if the value entered by the user is numeric"""
	try:
		int_num = int(number)
		isinstance(int_num,int)
	except:
		print "This is not a number, please start over"
		exit(0)
	else:
		return int_num
		
def main(): 
	print "Let's play the mimsmind0 game."
	num_of_tries = 0
	num_of_digits_raw = get_num_of_digits()
	num_of_digits = check_for_num(num_of_digits_raw)
	
	magic_num = random.randint(10**(num_of_digits-1), 10**num_of_digits-1)
	print magic_num
		
	while True:	
		num_of_tries += 1
		if num_of_tries == 1:
			print "Guess a",num_of_digits,"digit number :",
		guessed_num_raw = raw_input()
		guessed_num = check_for_num(guessed_num_raw)
		if len(guessed_num_raw) != num_of_digits:
			print "Please enter a",num_of_digits,"digit number :"
		else:
			if guessed_num == magic_num:
				print "Congratulations. You guessed the correct number in",num_of_tries,"tries."
				break
			elif (guessed_num < magic_num):
				print "Try again. Guess a higher number:",  
				
			else:
				print "Try again. Guess a lower number:",
		 
	

	
if __name__ == '__main__':
    main()