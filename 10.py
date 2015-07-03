def findPrimes(n):
	primes = set(range(2, n+1))
	nums = range(2, n+1)
	for a in nums:
		p = a
		p += a
		while p <= n:
			if p in primes:
				primes.remove(p)
			p += a
	print sum(primes)
	return primes

