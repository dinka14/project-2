inp_string = input().split()

occur_before = set()

for i in inp_string:
    if i in occur_before:
        print('YES')
    else:
        print('NO')
        occur_before.add(i)

