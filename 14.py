
# -*- coding: utf-8 -*-
"""Longest Collatz sequence
Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""


# more interesting: longest chain before diminishing
# 3n+1 % 3 cycles, then will hit double n/2?

# number : count
cache = {1: 1} # Base case

def next_number(n):
    if n%2 == 0:
        return n/2
    return 3*n+1

def collatz_gen(n):
    while True:
        if n == 1:
            raise StopIteration
        if n%2 == 0:
            n /= 2
        else:
            n = 3*n+1
        yield n

def collatz_seq(n):
    return [n, ] + [x for x in collatz_gen(n)]

def collatz_length(n):
    size = 0
    n_0 = n
    while 1: # Conjecture is that it will always end.
        # Assumes {1: 1} is always in cache
        if n in cache:
            size += cache[n]
            cache[n_0] = size  # Add result to cache
            return size
        else:
            size += 1
            n = next_number(n)

def biggest_chain_up_to(biggest_n = 100):
    max_size = 1
    max_size_number = 1
    for x in xrange(1, biggest_n+1):
        sequence_size = collatz_length(x)
        if sequence_size > max_size:
            max_size = sequence_size
            max_size_number = x
    # print "Max size: %d, for number %d" % (max_size, max_size_number)
    return (max_size, max_size_number) 

# import pdb; pdb.set_trace()
print biggest_chain_up_to(999999)
# (525, 837799)
# Max size: 686, for number 8400511, given 10 million

# Note: Could have memoized collatz_length and called recursively. Sadly, i think that would have been slower
