'''
Find the thirteen adjacent digits in the 1000-digit 
number that have the greatest product. 
What is the value of this product?
'''

def largest_product():
	temp = 0
	file = open('../data/008_number.txt')
	number = int(file.read())
	for x in range(1, 988):
		s = 1
		n = 0
		tempNum = number
		while n < 13:
			s *= tempNum % 10
			tempNum /= 10
			n += 1
		if s > temp:
			temp = s
		number /= 10
	return temp

print(largest_product())
