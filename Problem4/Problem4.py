# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindromic(number):
    digits = [int(i) for i in str(number)]
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False


num = 0
for a in range(999, 100, -1):
    for b in range(a, 100, -1):
        x = a * b
        if x > num:
            if is_palindromic(a * b):
                num = x
print(num)
