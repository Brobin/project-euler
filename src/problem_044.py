'''
Find the pair of pentagonal numbers, Pj and Pk, for which 
their sum and difference are pentagonal and D = |Pk - Pj| 
is minimised; what is the value of D?
'''

from functions import pentagonal_number, is_pentagonal

def pentagonal_diff():
	i = 1
	while True:
		i += 1
		n = pentagonal_number(i)
		for j in reversed(range(1, i-1)):
			m = pentagonal_number(j)
			if is_pentagonal(n-m) and is_pentagonal(n+m):
				return n-m

print(pentagonal_diff())

