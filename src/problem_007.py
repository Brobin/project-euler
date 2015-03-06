'''
What is the 10001st prime number?
'''

from shared import is_prime
 
def nth_prime(n):
    prime = 2
    count = 1
    iter = 3
    while count < n:
        if is_prime(iter):
            prime = iter
            count += 1
        iter += 2
    return prime

print(nth_prime(10001))
