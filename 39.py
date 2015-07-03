'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
'''
import math
import time

start = time.time()
# to find a program w/ integral we want to iterate up from a and b
max_p = 1000


p_solutions = {num: set([]) for num in xrange(max_p+1)}

max_side = int(max_p) + 1
for a in xrange(1, max_p/3 + 1):
    a_squared = a**2
    for b in xrange(1, max_p/2 + 1):
        c = math.sqrt(a_squared + b**2)
        if not c.is_integer(): continue
        p = a + b + c
        if p > max_p: break
        p_solutions[p].add(frozenset([a,b,c]))

print max(p_solutions.keys(), key=lambda x: len(p_solutions[x]))


end = time.time()
print end - start