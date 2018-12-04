input_string = '1 2 3 2 3 4'
new_set = set(input_string.split())
print(new_set)
super_set = set(input_string[0])
for i in input_string:
    for j in super_set:
        if i != j:
            super_set.add(i)
        else:
            print('YES')
            break
    print('NO')

print(super_set)

# if number_meet_before
# than Yes
# else No
