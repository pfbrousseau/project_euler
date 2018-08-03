#!/bin/python

import sys
CACHE = dict()
def fib():
    a, b = 0, 1
    while True:            # First iteration:
        yield a            # yield 0 to start with and then
        a, b = b, a + b

t = int(raw_input().strip())
for a0 in xrange(t):
    numbers = []
    running_sum = 0
    max_n = long(raw_input().strip())
    if max_n in CACHE:
        print CACHE[max_n]
    else:
        
        for n in fib():
            if n%2 == 0:
                #numbers.append(n)
                running_sum += n
                CACHE[n] = running_sum
            if n > max_n:
                #print CACHE[n]
                break
        print CACHE[max_n]