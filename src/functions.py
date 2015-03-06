'''
Useful mathmatical functions that may be used
for multiple solutions.
'''

import math

def is_prime(n):
	n = abs(n)
	for x in range(3, int(n**0.5)+1, 2):
		if n % x == 0:
			return False
	return True

def triangular_number(n):
	'''
	Calculates the triangular number of the
	given size.
	'''
	return n*(n+1)/2

def is_triangular(number):
	'''
	Determines whether the given number is
	triangular.
	'''
	x = math.sqrt(8*number+1)
	return x.is_integer()

def pentagonal_number(n):
	'''
	Calculates the pentagonal number of the
	given size.
	'''
	return n*(3*n-1)/2

def is_pentagonal(number):
	'''
	Determines whether the given number is
	pentagonal.
	'''
	x = (math.sqrt(1 + 24*number) + 1.0) / 6.0
	return x.is_integer()

def hexagonal_number(n):
	'''
	Calculates the hexagonal number of the
	given size.
	'''
	return n*(2*n-1)

def is_hexagonal(number):
	'''
	Determines whether the given number is
	hexagonal.
	'''
	x = (math.sqrt(8*number + 1) + 1.0) / 4.0
	return x.is_integer()

def collatz(n):
	'''
	Returns the Collatz sequence starting at a
	number. The Collatz sequnce is as follows:
	If the current value is even, the next value
	is the current divided by 2. If it is odd, the
	next value is 3 times the curent + 1.
	Although it hasn't been proven, it is believed
	that the sequnce will end at 1 for any number.
	'''
	sequence = [n]
	while n != 1:
		if n % 2 == 0:
			n = n/2
		else:
			n = 3*n + 1
		sequence.append(n)
	return sequence

def fibonacci(n):
	'''
	Returns n values of the fibonacci series
	'''
	sequence = [0,1]
	while len(sequence) < n:
		l = len(sequence)
		x = sequence[l-2] + sequence[l-1]
		sequence.append(x)
	return sequence

def divisors(number):
	'''
	Finds the all divisors of a given number
	'''
	divisors = []
	for x in range(1, number):
		if number % x == 0:
			divisors.append(x)
	return divisors

def amicable_number(n):
	'''
	Finds whether a number is amicable. A number is 
	part of an amicable pair if the following is true
	b =  sum of a's divisors
	a = sum of b's divisors
	'''
	x = sum(divisors(n))
	y = sum(divisors(x))
	return n == y and n != x

def triangle_max_path(t):
	'''
	Calculates the maximum path through a triangle
	represented as a two dimensional list.
	'''
	depth = len(t) - 1
	while depth != 0:
		for x in range(len(t[depth])-1):
			t[depth-1][x] += max(t[depth][x], t[depth][x+1])
		t.pop()
		depth = len(t) - 1

	return t[0][0]
