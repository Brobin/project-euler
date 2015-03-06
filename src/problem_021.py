'''
Evaluate the sum of all the amicable numbers under 10000.
'''

from functions import amicable_number

def sum_amicable_numbers(n):
	total = 0
	for x in range(n):
		if amicable_number(x):
			total += x
	return total

print(sum_amicable_numbers(10000))
