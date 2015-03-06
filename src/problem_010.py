'''
Find the sum of all the primes below two million.
'''

from functions import is_prime

def sum_prime(num):
	sum_prime = 0
	for x in range(1, num):
		if is_prime(x):
			sum_prime += x
	return sum_prime

print sum_prime(2000000)
