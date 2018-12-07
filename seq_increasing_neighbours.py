first_elem = int(input())
second_element = -1
count = 0
while second_element != 0:
    second_element = int(input())
    print(second_element)
    if first_elem < second_element:
        print(first_elem)
        count += 1
        first_elem = second_element
print(count)
