def find_super_parent(rod_dict):
    for i in rod_dict.values():
        if i not in rod_dict.keys():
            height_dict[i] = 0
            break
    return i


'''
num = int(input())
rod_dict = {}

for _ in range(num - 1):
    child, parent = input().split()
    rod_dict[child] = parent

'''

rod_dict = {'Alexei': 'Peter_I', 'Anna': 'Peter_I', 'Elizabeth': 'Peter_I', 'Peter_II': 'Alexei', 'Peter_III': 'Anna',
            'Paul_I': 'Peter_III', 'Alexander_I': 'Paul_I', 'Nicholaus_I': 'Paul_I'}
print(rod_dict)

height_dict = dict()

super_parent = find_super_parent(rod_dict)
new_parent_list = [super_parent]
while new_parent_list:  # not empty
    for key, value in rod_dict.items():
        if rod_dict[key] in new_parent_list:
            height_dict[key] = height_dict.get(key, 0) + 1
        new_parent_list.append(key)


print(height_dict, sorted(new_parent_list))
