fact_memo = {1: 1, 0: 1}


def fact(n):
    if n in fact_memo:
        return fact_memo[n]
    result = n*fact(n-1)
    fact_memo[n] = result
    return result


def c(n, r):
    return fact(n) / fact(r) / fact(n-r)

count = 0
for n in xrange(1, 101):
    for r in xrange(1, n):
        if c(n, r) > 10**6:
            count += 1

print count
