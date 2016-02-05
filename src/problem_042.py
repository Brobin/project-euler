'''
By converting each letter in a word to a number 
corresponding to its alphabetical position and 
adding these values we form a word value.
Using words.txt, how many are triangle words?
'''

from functions import is_triangular


def word_value(word):
    value = 0
    for c in word:
        value += ord(c) - 64
    return value


def num_triangle_words():
    triangles = 0
    words = open('../data/042_words.txt').read()
    words = words.replace('"', '').split(',')
    for word in words:
        value = word_value(word)
        if is_triangular(value):
            triangles += 1
    return triangles

print(num_triangle_words())
