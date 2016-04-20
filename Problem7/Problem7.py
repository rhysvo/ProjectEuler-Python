

def primes(n):
    prime_nums = [2]
    attempt = 3
    while len(prime_nums) < n:
        if all(attempt % prime != 0 for prime in prime_nums):
            prime_nums.append(attempt)
        attempt += 2
    return prime_nums[-1]

print(primes(10001))