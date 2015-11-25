# number chain

# every number chain ends at 1 or 89


def next_link(n):
    return sum(map(lambda x: int(x)**2, list(str(n))))

seen = {}


def at_89(n):
    trail = set()
    trail.add(n)
    while True:
        if n in seen:
            for num in trail:
                seen[num] = seen[n]
            return seen[n]
        if n == 1:
            for num in trail:
                seen[num] = 0
            return 0
        if n == 89:
            for num in trail:
                seen[num] = 1
            return 1
        n = next_link(n)
        trail.add(n)

ten_million = 10**7
#print sum(map(at_89, xrange(1, ten_million)))
