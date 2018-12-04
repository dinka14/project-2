with open('input.file', 'r') as f:
    amount = f.read().splitlines()
    anna_cubes = amount[0].split()[0]
    boris_cubes = amount[0].split()[1]

anna_set = set()
boris_set = set()

for i in range(1, int(anna_cubes) + 1):
    anna_set.add(amount[i])

for i in range(int(anna_cubes) + 1, len(amount)):
    boris_set.add(amount[i])

print(len(anna_set & boris_set))
print(*sorted(anna_set & boris_set, key=int))
print(len(anna_set - boris_set))
print(*sorted(anna_set - boris_set, key=int))
print(len(boris_set - anna_set))
print(*sorted(boris_set - anna_set, key=int))
