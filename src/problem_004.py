'''
Find the largest palindrome made from 
the product of two 3-digit numbers.
'''

def palindrome_3_digit():
	temp = 0
	p = 0
	for x in range(100, 999):
		for y in range(100, 999):
			temp = x * y
			if str(temp) == str(temp)[::-1] and temp > p:
				p = temp
	return p

print(palindrome_3_digit())
