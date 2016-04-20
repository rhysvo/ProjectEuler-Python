prime_filter = [True] * 2000000


def mark(primes, x):
    for i in range(x + x, len(primes), x):
        primes[i] = False


for x in range(2, int(len(prime_filter) ** 0.5) + 1):
    if prime_filter[x]:
        mark(prime_filter, x)

print(sum(i for i in range(2, len(prime_filter)) if prime_filter[i]))
