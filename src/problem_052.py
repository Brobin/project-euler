'''
It can be seen that the number, 125874, and its double, 
251748, contain exactly the same digits, but in a different order.
Find the smallest positive integer, x, such that 2x, 
3x, 4x, 5x, and 6x, contain the same digits.
'''

def permuted_multiples(n):
	x = 1
	while True:
		done = [same_digits(x, x*z) for z in range(2,n+1)]
		if all(t for t in done):
			return x
		x += 1

def same_digits(num1, num2):
	return sorted(str(num1)) == sorted(str(num2))

print(permuted_multiples(6))
