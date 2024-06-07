"""
File: quadratic_solver.py
Name: Jessie
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	Compute the roots of equation.
	"""
	print('stanCode Quadratic Solver!')
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))
	x = b*b-4*a*c
	if x > 0:                         # 2 roots
		y = math.sqrt(x)
		d = (-b + y) / (2 * a)
		e = (-b - y) / (2 * a)
		print('Two roots: '+str(d)+ ', ' +str(e))
	elif x == 0:                      # 1 root
		f = -b / (2 * a)
		print('One root: '+str(f))
	else:
		print('No real roots')


if __name__ == "__main__":
	main()
