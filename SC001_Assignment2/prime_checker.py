"""
File: prime_checker.py
Name: Jessie
-----------------------
This program asks our user for input and checks if the input is a
prime number or not. First, ” Welcome to the prime checker” will be printed on Console.
And the program will continually ask the user to enter an integer 
that is greater than 1 and checks if it is a prime number.
The program ends when the user enter the EXIT number.
"""


# This constant controls when to stop
EXIT = -100


def main():
	"""
	This program will check if it is a prime number.
	"""
	print('Welcome to the prime checker! ')
	while True:
		n = int(input('n: '))
		if n == EXIT:
			print('Have a good one! ')
			break
		if is_prime(n):
			print(str(n)+ ' is a prime number.')
		else:
			print(str(n)+ ' is not a prime number.')


def is_prime(n):
	if n <= 1:
		result = False
	i = 2
	result = True
	while i <= int(n ** 0.5):
		if n % i == 0:
			result = False
			break
		i += 1
	return result







# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
