"""
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(n):
    n = str(n)
    return n == n[::-1]

# Sanity check
assert is_palindrome(9009)

largest = 0
for x in xrange(900, 1000):
    for y in xrange(900, 1000):
        test_n = x*y
        if is_palindrome(test_n):
            if test_n > largest:
                largest = x*y

print largest

