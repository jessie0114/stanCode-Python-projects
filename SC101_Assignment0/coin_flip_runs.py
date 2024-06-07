"""
File: coin_flip_runs.py
Name: Jessie
-----------------------
This program should simulate coin flip(s)
with the number of runs input by users.
A 'run' is defined as consecutive results
on either 'H' or 'T'. For example, 'HHHHHTHTT'
is regarded as a 2-run result.
Your program should stop immediately after your
coin flip results reach the number of runs!
"""

import random as r


def main():
	"""
	This program will flip the coin until flip results
	reach the number of runs entered by the user.
	"""
	print("Let's flip a coin!")
	# Asking the user to enter the number of runs.
	num_run = int(input('Number of runs: '))
	# Setting initial conditions before looping the runs counting loop.
	result = ''      # Recording all the flip results. Starting with empty string.
	number = 0       # Counting the number of runs.
	if_run = False   # The status of whether the result is consecutive.
	# The loop won't stop unless the flip results reaches the runs set by the user.
	while num_run != number:
		coin = flip()                # The new flip result.
		result += coin               # Recording all the flip results.
		if len(result) > 1:          # Checking process of runs starts with 2nd flip.
			last = result[len(result) - 2]  # The last result before this new result.
			# Checking whether the new flip result equals the last one.
			if last == coin:         # True. The result is consecutive.
				# Checking whether this consecutive result is a new run.
				if not if_run:       # True. When if_run is False, this is a new run.
					if_run = True    # Turning if_run into True to start this run.
					number += 1      # The number of runs increases by 1.
			else:                    # False. The result is not consecutive.
				if_run = False       # if_run must be False if not consecutive.
	print(result)  # Printing out all the flip results when the loop ends.


def flip():
	"""
	This function randomly flips the coin and returns the flip result.
	:return coin: the flip result, either 'H' or 'T'.
	"""
	num = r.randint(0, 1)   # Randomly flipping the coin.
	coin = ''  # Empty string. Recording the flip result.
	# Assigning the flip result based on the random flip.
	if num == 0:
		coin = 'T'
	coin += 'H'
	return coin              # Returning the flip result.
	

if __name__ == "__main__":
	main()
