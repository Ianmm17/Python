"""
Digital Cypher

Write a function that accepts str string and key number and returns an array of integers representing encoded str.

Digital Cypher assigns to each letter of the alphabet unique number.
Then we add to each obtained digit consecutive digits from the key.
"""


# https://www.codewars.com/kata/592e830e043b99888600002d/train/python

def encode(message, key):
    for i in message:
        print(message[i])
    return message, key


print(encode("scout", 1939))
