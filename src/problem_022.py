'''
Using names.txt, begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in 
the list to obtain a name score.What is the total 
of all the name scores in the file?
'''

def name_scores():
	names = open('../data/022_names.txt').read()
	names = names.replace('"', '').split(',')
	names = sorted(names)
	total = 0
	count = 1
	for name in names:
		score = 0
		for c in name:
			score += ord(c) - 64
		total += score * count
		count += 1
	return total

print(name_scores())
