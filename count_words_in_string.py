from collections import Counter

with open('input.file', 'r', encoding='utf-8') as infile:
    words = [word for line in infile for word in line.split()]
    print(words)
    print(Counter(words))

string = 'Hello Hello I\'m a string'
print((Counter(string.split())))
