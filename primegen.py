# Use `pyprimes` instead of my own code. It is much faster

primes = [2,]

def is_prime(n):
    return all([n%prime for prime in primes])

def prime_generator():
    yield 2
    a = 3
    while 1:
        if is_prime(a):
            primes.append(a)
            yield a
        a += 2

def test():
    prime = prime_generator()
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    result = [prime.next() for _ in xrange(len(expected))]
    assert expected == result, "Primes did not match expected:\n Expected: \t%s,\n Got: \t\t%s" % (expected, result)
    print "pass"
