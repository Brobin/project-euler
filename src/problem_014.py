'''
Which starting number, under one million, 
produces the longest collatz sequnce?
'''

from functions import collatz

def longest_collatz(n):
	longest = 0
	number = 0
	for x in range(1, n+1):
		length = len(collatz(x))
		if length > longest:
			longest = length
			number = x
	return number

print(longest_collatz(1000000))
