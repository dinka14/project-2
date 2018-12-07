a = [int(s) for s in input().split()]
k, C = input().split()
a.append(0)
print(a, len(a))
for i in range(int(k) + 1, len(a)):
    a[i - 1] = a[i]
a[int(k)] = int(C)
