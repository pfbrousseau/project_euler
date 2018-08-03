from pyprimes import factors, factorise


"""
Highly divisible triangular number
Problem 12
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""

# def get_divisors_slow(n):
#     [1,] + [d for d in xrange(1,n) if n%d==0]

def count_divisors(n):
    factorise_gen = factorise(n)
    # factor_list = list(factorise_gen)
    c = 1
    for root, rank in factorise_gen:
        c *= rank+1 # Multiply prime's exponents +1 to get count of pairs
    return c

def triangle_number():
    n, i = 0, 0
    while 1:
        i += 1 # Could use a counter, but don't remember by heart
        n += i
        yield n

# Replaced by pyprimes
# factorise_gen = factorise(n)
    # factor_list = get_divisors_slow(n) #[f for f in factorise_gen]
    # print n, factor_list
    # if len(factor_list) == 5-1:
    #     print n
    #     break

    # i += 1
    # n += i

number_gen = triangle_number()
while 1:
    n = number_gen.next()
    c = count_divisors(n)
    if c >= 500:
        print n, c
        break

