'''
How many distinct terms are in the sequence generated 
by ab for 2 <= a <= 100 and 2 <= b <= 100?
'''


def distinct_terms():
    terms = []
    for x in range(2, 101):
        for y in range(2, 101):
            terms.append(x**y)
    terms = list(set(terms))
    return len(terms)

print(distinct_terms())
