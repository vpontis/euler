import math

def func():
	c = 999
	cdiv = c/100
	while c > 1:
		a = 1
		while a < math.sqrt(c):
			b = 1000 - c - a
			if b <= 0:
				break
			print (a, b, c)
			if a**2 + b**2 == c**2:
				return (a, b, c)
			a += 1
		c -= 1
	return None

def oth():
	for c in range(1, 1000):
		for b in range(1, c):
			a = 1000 - b - c
			if a**2 + b**2 == c**2:
				return a*b*c

if __name__ == '__main__':
	print oth()
