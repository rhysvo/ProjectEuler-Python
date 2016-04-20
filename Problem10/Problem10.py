# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.


def mark_as_not_prime(primes, x):
    for i in range(x + x, len(primes), x):
        primes[i] = False


prime_filter = [True] * 2000000

for x in range(2, int(len(prime_filter) ** 0.5) + 1):
    if prime_filter[x]:
        mark_as_not_prime(prime_filter, x)

print(sum(i for i in range(2, len(prime_filter)) if prime_filter[i]))
