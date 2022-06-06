"""
We want to know the index of the vowels in a given word, for example, there are two vowels in the word super (the second and fourth letters).

So given a string "super", we should return a list of [2, 4].

This is indexed from [1..n] (not zero indexed!)
"""


def vowel_indices(word):
    vowels = ["a", "e", "i", "o", "u", "y"]

    index_vowel = []
    for i, letter in enumerate(word):
        for vowel in vowels:
            if letter.upper() == vowel.upper():
                index_vowel.append(i + 1)
    return index_vowel


print(vowel_indices('YoMama'))
