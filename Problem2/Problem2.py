fib_numbers = {}


# Recursive Method for finding fibonacci
def fib_sequence(n):
    fib_numbers[n] = fib_numbers.get(n, 0) or \
                     (n <= 1 and 1 or fib_sequence(n - 1) + fib_sequence(n - 2))
    return fib_numbers[n]


n = 0
i = 0
while fib_sequence(i) <= 4000000:
    if not fib_sequence(i) % 2:
        n = n + fib_sequence(i)
    i += 1
print(n)
