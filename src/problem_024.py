'''
A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of 
the digits 1, 2, 3 and 4. What is the millionth 
lexicographic permutation of the digits 
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

def permutations(items):
	if len(items) == 2:
		return [''.join(items), ''.join(items[::-1])]
	result = []
	for i in range(len(items)):
		perms = permutations(items[:i] + items[i + 1:])
		for p in perms:
			result.append(items[i] + p)
 
	return result

perms = permutations([c for c in '0123456789'])
print(perms[999999])
