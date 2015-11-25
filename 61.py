def generic_generator(n, func):
    i = 1
    num = func(i)
    while num <= n:
        yield num
        i += 1
        num = func(i)


def triangles(n):
    return generic_generator(n, lambda i: i*(i+1)/2)


def squares(n):
    return generic_generator(n, lambda i: i**2)


def pentagons(n):
    return generic_generator(n, lambda i: i*(3*i-1)/2)


def hexagons(n):
    return generic_generator(n, lambda i: i*(2*i-1))


def heptagons(n):
    return generic_generator(n, lambda i: i*(5*i-3)/2)


def octagons(n):
    return generic_generator(n, lambda i: i*(3*i-2))


def with_prefix(prefix, nums):
    return filter(lambda num: num / 10**2 == prefix, nums)

possible_triangles = set(triangles(10**4)) - set(triangles(10**3))
possible_squares = set(squares(10**4)) - set(squares(10**3))
possible_pentagons = set(pentagons(10**4)) - set(pentagons(10**3))
possible_hexagons = set(hexagons(10**4)) - set(hexagons(10**3))
possible_heptagons = set(heptagons(10**4)) - set(heptagons(10**3))
possible_octagons = set(octagons(10**4)) - set(octagons(10**3))

possibilities = [possible_heptagons, possible_hexagons, possible_pentagons, possible_squares, possible_triangles]

from itertools import permutations, repeat
from collections import deque
for octagon in possible_octagons:
    oct_pre = octagon / 10**2
    oct_suf = octagon % 10**2
    for possibility in permutations(possibilities):
        q = deque(map(lambda x: (x,[x]), with_prefix(oct_suf, possibility[0])))
        nextq = deque()
        depth = 1
        while depth < len(possibility):
            while q:
                num, path = q.popleft()
                num_suf = num % 10**2
                nextq.extend(map(lambda x: (x, path[:] + [x]), with_prefix(num_suf, possibility[depth])))
            depth += 1
            q = nextq
            nextq = deque()
        if q and filter(lambda (x, _): x % 10**2 == oct_pre, q): 
            print q, oct_pre
            print sum(q[0][1])+octagon




      


