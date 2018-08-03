from math import sqrt

"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""


# print [(a,b,c) for a in xrange(1,340) for b in xrange(a,340) for c in xrange(b,1000) if (a**2 + b**2 == c**2) and a+b+c==1000 ]

def get_c_int(a,b):
    c = sqrt(a**2 + b**2)

    # Check if c is a perfect square's root
    if c != int(c):
        return None
    return c

def is_1000_triplet(a,b,c):
    return a + b + c == 1000

def run():
    for a in xrange(1,332):
        for b in xrange (a, 499):
            c = get_c_int(a,b)
            if c and is_1000_triplet(a, b, c):
                return (a, b, c), a*b*c

print run()