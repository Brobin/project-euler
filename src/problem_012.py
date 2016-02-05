'''
What is the value of the first triangle number 
to have over five hundred divisors?
'''

from functions import triangular_number, divisors


def triangle_divisors(n):
    # brute force and slow, but it works
    number = 0
    value = 0
    done = False
    while not done:
        value = triangular_number(number)
        print(value)
        done = len(divisors(value)) > n
        number += 1
    return value

print(triangle_divisors(500))
