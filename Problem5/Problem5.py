# 2520 is the smallest number that can be divided by each of the numbers
# from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20?


def lowest_common_multiple(x, y):
    return x * y / greatest_common_denominator(x, y)


def greatest_common_denominator(a, b):
    return b and greatest_common_denominator(b, a % b) or a

n = 1
for i in range(1, 21):
    n = lowest_common_multiple(n, i)

print(n)
