'''
Find the difference between the sum of the squares 
of the first one hundred natural numbers 
and the square of the sum.
'''

def dif_sum_square(num):
	sumSquares = 0
	sums = 0
	for y in range(1, num + 1):
		sums += y
		sumSquares += y ** 2
	sums = sums ** 2
	return sums - sumSquares

print(dif_sum_square(100))
