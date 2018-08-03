"""
Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""

# from primegen import prime_generator
# prime = prime_generator()

from pyprimes import primes
prime = primes()

prime_sum = 0
while 1:
    p = prime.next()
    if p > 2e6:
        break
    prime_sum += p
    print p

print prime_sum
