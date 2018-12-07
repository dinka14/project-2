def fib(n):
    if n == 0:
        return 0
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b


fib_number = 0
i = 0
A = int(input())
not_a_fib = 0
while fib_number != A:
    if fib_number > A:
        not_a_fib = -1
        print(not_a_fib)
        break
    fib_number = fib(i)
    i += 1

if not_a_fib != -1:
    print(i-1)