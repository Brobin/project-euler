'''
By considering the terms in the Fibonacci sequence 
whose values do not exceed four million, 
find the sum of the even-valued terms.
'''

def fibonacci(n):
	'''
	Returns the values of the fibonacci series
	up to a number n
	'''
	sequence = [0,1]
	done = False
	while not done:
		l = len(sequence)
		x = sequence[l-2] + sequence[l-1]
		if x > n:
			done = True
		else:
			sequence.append(x)
	return sequence

def sum_fibonacci_even(n):
	values = fibonacci(n)
	values = [v for v in values if v % 2 == 0]
	return sum(values)

print(sum_fibonacci_even(4000000))
