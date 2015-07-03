'''
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,
'''

from time import time

start_time = time()

def fact(n):
  tot = 1
  for i in range(1, int(n) + 1):
    tot *= i
  return tot


def comb(n, r):
    return fact(n)/(fact(r)*fact(n-r))


one_million = 10**6
c_over_million = set()

for n in range(23, 101):
    for r in range(0, (n+1)/2):
        c = comb(n, r)
        if c > one_million:
            c_over_million.add(c)

print len(c_over_million)

end_time = time()
print 'Took this many seconds:', end_time - start_time