'''
There exists exactly one Pythagorean triplet 
for which a + b + c = 1000.
Find the product abc.
'''


def pythagorean_triplet():
    for x in range(1, 500):
        for y in range(1, 500):
            z = (y**2 + x**2)**0.5
            if x + y + z == 1000:
                return int(x * y * z)

print(pythagorean_triplet())
