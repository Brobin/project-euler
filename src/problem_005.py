'''
What is the smallest positive number that is evenly 
divisible by all of the numbers from 1 to 20?
'''

def divisible_in_range(start, end, num):
	for x in range(start, end+1):
		if num % x != 0:
			return False
	return True

def smallest_multiple(step):
    for num in xrange(step, 999999999, step):
        if divisible_in_range(1, step, num):
            return num
    return "No answer found"

print(smallest_multiple(20))
