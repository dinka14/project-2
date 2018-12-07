elem = int(input())
maxx = 0
count = 0
max_count = 0
while elem != 0:
    if elem > maxx:
        maxx = elem
        elem = int(input())
        max_count = count
    count += 1
print(max_count)

max = 0
index_of_max = -1
element = -1
len = 0
while element != 0:
    element = int(input())
    if element > max:
        max = element
        index_of_max = len
    len += 1
print(index_of_max)