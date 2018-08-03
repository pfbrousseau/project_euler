"""
10001st prime
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

primes = [2, ]

def is_prime(n):
    return all([n%prime for prime in primes])

def prime_gen_list_and_find():
    max_num = 10**12  # A big integer
    for a in xrange(3, max_num, 2):
        if is_prime(a):
            primes.append(a)
            if len(primes) == 10001:
                return a

# print is_prime(3)
print prime_gen_list_and_find()
