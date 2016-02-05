'''
What is the first term in the Fibonacci 
sequence to contain 1000 digits?
'''


def digit_fib(n):
    count = 1
    x = 0
    y = 1
    while len(str(y)) < n:
        temp = x
        x = y
        y += temp
        count += 1
    return count

print(digit_fib(1000))
