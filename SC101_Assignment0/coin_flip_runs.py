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
	This program will stop immediately after coin flip results reach the number of runs.
	"""
	print("Let's flip a coin! " )
	num = int(input('Number of runs: '))
	run = 0

	if run == num:
		break
	else:
		is_in_a_row = False
		roll1 = random.range(1,7)
		run = 0
		is_in_a_row = False
		for i in range(Num_Rolls-1):
			roll2 = random.random.randrange(1,7)
			if roll1 == roll2:
				if is_in_a_row == False:
					run += 1
					is_in_a_row = True
			else:
				is_in_a_row = False




# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == "__main__":
	main()
