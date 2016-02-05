'''
Starting in the top left corner of a 2x2 grid, and 
only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20x20 grid?
'''


def lattice_paths(size):
    # cube represents the diagonal through the center
    # of the lattice. Each cube point is the starting
    # point of one path
    cube = [1] * size
    # iterate down to the corner
    for x in range(size):
        # iterate to the sides
        for y in range(x):
            # sum up all of the surrounding paths
            cube[y] = cube[y] + cube[y - 1]
        # add those paths to the middle
        cube[x] = 2 * cube[x - 1]
    # return the bottom right corner
    return cube[size - 1]

print(lattice_paths(20))
