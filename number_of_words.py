import math

with open('input.file', 'r') as file:
    words = [word for line in file for word in line.split()]
    print(len(set(words[1:])))

print(math.factorial(5))