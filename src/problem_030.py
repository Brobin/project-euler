'''
Find the sum of all the numbers that can be written
as the sum of fifth powers of their digits.
'''


def equals_fifth_powers(number):
    string = str(number)
    total = 0
    for c in str(number):
        total += int(c)**5
    return number == total


def fifth_powers():
    yup = []
    for x in range(1000, 1000000):
        if equals_fifth_powers(x):
            yup.append(x)
    return sum(yup)

print(fifth_powers())
