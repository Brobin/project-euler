'''
Work out the first ten digits of the sum of 
the one-hundred 50-digit numbers in 013_numbers.txt
'''

def last_ten():
	file = open('../data/013_numbers.txt')
	numbers = []
	for line in file:
		numbers.append(int(line))
	total = sum(numbers)
	return str(total)[:10]

print(last_ten())
