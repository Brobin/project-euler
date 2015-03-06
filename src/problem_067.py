'''
Find the maximum total from top to bottom in triangle.txt, 
a text file containing a triangle with one-hundred rows.
'''

from functions import triangle_max_path

def run_sum_path():
	t = open('../data/067_triangle.txt')
	triangle = []
	for line in t:
		values = line.replace('\n', '').split(' ')
		values = [int(v) for v in values]
		triangle.append(values)
	return triangle_max_path(triangle)

print(run_sum_path())
