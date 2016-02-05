'''
What is the largest prime factor of the number 600851475143?
'''


def prime_factors(n):
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d += 1

    return max(factors)

n = 600851475143
print(prime_factors(n))
