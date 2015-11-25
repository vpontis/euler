# we know a fraction is divisible by anything it shares common factors with
# so what we can do is find out the prime factorization of the number
# then we want to know how many numbers the prime numbers knock off
# so we take multiples of the prime numbers up to the frac and store that in a set
# 1-len(set) is going to be the num

import numpy
import math


def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n/3 + (n%6==2), dtype=numpy.bool)
    for i in xrange(1,int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k/3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)/3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]


from fractions import gcd

primes = primesfrom2to(10**8)
prime_set = set(primes)

goal = 15499/94744.0


def resilience(frac):
    count = 1
    for num in xrange(2, frac):
        if gcd(num, frac) > 1:
            count += 1
    return 1-float(count)/(frac-1)


def totient(n):
    tot = n
    for prime in primes:
        if prime >= n:
            break
        if n % prime == 0:
            tot *= 1-1/float(prime)
    return tot


def resil(frac):
    not_resil_set = set()
    if frac in prime_set:
        return 1-float(1)/(frac-1)
    for prime in primes:
        if prime > frac:
            break
        if gcd(prime, frac) > 1:
            num = prime
            while num < frac:
                not_resil_set.add(num)
                num += prime
    return 1-float(len(not_resil_set))/(frac-1)


def r(n):
    return 1-(n-totient(n)-1)/float(n-1)


def search_for_resil(n):
    for i in xrange(12, n):
        if r(n) < goal:
            print n


import cProfile
# cProfile.run('search_for_resil(10000)')
