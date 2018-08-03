"""
Multiples of 3 and 5
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
print sum([x for x in xrange(0, 1000) if (x%3==0 or x%5==0)])

# Alternative to xrange(0, 1000) would be (set(3 * range) + set(5 * range)), where range loops 1000/3, 1000/5 times
# Or multiples of 3 + multiples of 5 (geometric sequence multiplied by 3 and 5), minus multiples of 15 (doubles)
