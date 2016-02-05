'''
Find the sum of the digits in the number 100!
'''

import math


def factorial_digit_sum(n):
    number = math.factorial(n)
    number_str = str(number)
    total = sum([int(x) for x in number_str])
    return total

print(factorial_digit_sum(100))
