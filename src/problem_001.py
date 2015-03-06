'''
Find the sum of all the multiples of 3 or 5 below 1000.
'''

def sum_multiples():
	sum = 0
	for x in range(0, 1000):
		if x % 3 == 0 or x % 5 == 0:
			sum += x
	return sum

print(sum_multiples())
