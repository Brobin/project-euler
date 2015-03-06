'''
Find the maximum total from top to bottom of 
the triangle in 018_triangle.txt
'''

from functions import triangle_max_path

def run_sum_path():
	t = open('../data/018_triangle.txt')
	triangle = []
	for line in t:
		values = line.replace('\n', '').split(' ')
		values = [int(v) for v in values]
		triangle.append(values)
	return triangle_max_path(triangle)

print(run_sum_path())
