'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to 
the sum of the factorial of their digits.
'''

import math

def digit_factorial(number):
	total = 0
	string = str(number)
	for c in string:
		total += math.factorial(int(c))
	return total

def total_digit_factorials():
	total = 0
	for x in range(2,50000):
		if x == digit_factorial(x):
			total += x
	return total

print(total_digit_factorials())
