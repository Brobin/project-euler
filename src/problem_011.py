'''
What is the greatest product of four adjacent numbers 
in the same direction (up, down, left, right, or diagonally) 
in a 20x20 grid?
'''


def file_to_matrix():
    m_file = open('../data/011_grid.txt')
    matrix = []
    for line in m_file:
        matrix.append([int(x) for x in line.split(' ')])
    return matrix


def find_greatest_product(matrix):
    m = matrix
    l = len(m)
    best = 0

    for x in range(0, l - 3):
        for y in range(0, l - 3):
            hori = m[x][y] * m[x][y + 1] * m[x][y + 2] * m[x][y + 3]
            vert = m[x][y] * m[x + 1][y] * m[x + 2][y] * m[x + 3][y]
            diag = m[x + 3][y] * m[x + 2][y + 1] * \
                m[x + 1][y + 2] * m[x][y + 3]
            diag2 = m[x][y] * m[x + 1][y + 1] * \
                m[x + 2][y + 2] * m[x + 3][y + 3]

            best = max(hori, vert, diag, diag2, best)

    return best

matrix = file_to_matrix()
print(find_greatest_product(matrix))
