def power(a, n):
    if n == 0:
        return 1
    elif n > 0:
        for i in range(n):
            a *= a
            return a
    elif n < 0:
        for i in range(n):
            a *= a
            return 1 / a


a = float(input())
n = int(input())
print(power(a, n))
