fib_1 = 1
fib = fib_1 + 1
i = 3

while(len(str(fib)) < 1000):
  new_fib = fib + fib_1

  fib_1 = fib
  fib = new_fib
  i += 1

print i

print fib