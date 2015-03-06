'''
What is the sum of the digits of the number 2^1000?
'''

def power_digit_sum(number, power):
	result = number**power
	result_str = str(result)
	total = sum([int(x) for x in result_str])
	return total

print(power_digit_sum(2, 1000))
