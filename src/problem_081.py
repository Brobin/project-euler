'''
Find the minimal path sum, in 081_matrix.txt from 
the top left to the bottom right by only moving right and down.

To do this one, I treated it like problem 67 but backwards. In 
problem 67 I found the maximum path through a triangle.

In this problem, I first split the matrix into two triangles. Then I 
iterate through each one and caluclate the minimum path to the middle
Then with those two arrays of minimums in the middle from both triangles
I am able to determing the overall minimum.
'''


def load_matrix():
    file = open('../data/081_matrix.txt')
    matrix = []
    for line in file:
        row = [int(x) for x in line.split(',')]
        matrix.append(row)
    return matrix


def upper_triangle(matrix):
    triangle = []
    for i in range(len(matrix)):
        row = []
        for j in range(i + 1):
            row.append(matrix[i - j][j])
        triangle.append(row)
    return triangle


def lower_triangle(matrix):
    new = []
    for i in range(len(matrix)):
        new.append(matrix[i][::-1])
    new = new[::-1]
    return upper_triangle(new)


def triangle_path(t):
    for depth in range(1, len(t)):
        for i in range(0, len(t[depth])):
            if i > 0 and depth > 1 and i < len(t[depth]) - 1:
                t[depth][i] += min(t[depth - 1][i - 1], t[depth - 1][i])
            elif i == len(t[depth]) - 1:
                t[depth][i] += t[depth - 1][i - 1]
            elif i == 0:
                t[depth][i] += t[depth - 1][i]
    return t[len(t) - 1]


def find_min(x, y, matrix):
    best = x[0] + y[0] - matrix[0][(len(matrix) - 1)]
    for i in range(len(x)):
        j = len(matrix) - 1 - i
        current = x[i] + y[i] - matrix[j][i]
        if current < best:
            best = current
    return best


def minimum_path():
    matrix = load_matrix()

    upper = upper_triangle(matrix)
    lower = lower_triangle(matrix)

    path_upper = triangle_path(upper)
    path_lower = triangle_path(lower)[::-1]

    return find_min(path_upper, path_lower, matrix)

print(minimum_path())
