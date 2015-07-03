def triag():
	triag = 1
	a = 2
	while True:
		triag += a
		a += 1
		if factor(triag) > 500:
			return triag

def factor(n):
	factors = 0
	i = 1
	while i <= n:
		if n % i == 0:
			factors += 1
		i += 1
	print factors
	return factors

