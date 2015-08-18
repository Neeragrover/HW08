import sys
import random

def get_num_of_digits():
	"""This function checks if the user provided the number if digits at the command line. If not, it prompts the user to enter it.
	It finally returns the user entered value"""
	if len(sys.argv) == 1:
		num_of_digits = 3
	else:
		num_of_digits = sys.argv[1]
	return num_of_digits
	
def check_for_num(number):
	""" This function checks if the value entered by the user is numeric"""
	try:
		int_num = int(number)
	except:
		return -1
	else:
		return int_num

def evaluate_bulls_cows(guessed_num_raw, str_magic_num,num_of_digits):
	"""This function evaluates and returns the number of bulls and cows."""
	guessed_list = list(guessed_num_raw)	#converting the strings to lists to check for bulls
	magic_list = list(str_magic_num)
	list_bulls = []
	cows = 0
	bulls = 0

# iterating the two lists to find matches and get a count of bulls	
	for i in range(num_of_digits):
		if guessed_list[i] == magic_list[i]:
			bulls += 1
			list_bulls.append(guessed_list[i])
			
#eliminating the bulls to find cows
	for item in list_bulls:
		guessed_list.remove(item)
		magic_list.remove(item)

#iterating the remaining lists to get a count for cows
	for item in guessed_list:
		if item in magic_list:
			cows += 1
							
	print bulls,"bull(s)",cows,"cow(s).",
	return bulls, cows
	
		
		
def main(): 
	num_of_tries = 0
	num_of_digits_raw = get_num_of_digits()
	num_of_digits = check_for_num(num_of_digits_raw)
	
	if (num_of_digits == -1):
		print "Invalid Input. Please start over"
		exit(0)
		
	maxrounds = (2**num_of_digits) + num_of_digits
	
	print "Let's play the mimsmind1 game. You have",maxrounds,"guesses."
	
	magic_num = random.randint(10**(num_of_digits-1), 10**num_of_digits-1)
	str_magic_num = str(magic_num)
#	print str_magic_num
	
	print "Guess a",num_of_digits,"digit number (# 1 ):",
			
	while (num_of_tries < maxrounds):	
		num_of_tries += 1
		
		if(num_of_tries > 1):
			print "Try again (#",num_of_tries,"):",
				
		guessed_num_raw = raw_input()
		guessed_num = check_for_num(guessed_num_raw)

		
		if ((guessed_num == -1) or (len(guessed_num_raw) != num_of_digits)):
			print "Invalid input.",
			continue
		else:
			bulls, cows = evaluate_bulls_cows(guessed_num_raw, str_magic_num,num_of_digits)
		
		if bulls != num_of_digits:
			bulls = 0
			cows = 0
		else:
			print "Congratulations. You guessed the correct number in",num_of_tries,"tries."
			exit(0)
	
	print "Sorry. You did not guess the number in",maxrounds,"tries.The correct number is",magic_num	
		
if __name__ == '__main__':
    main()