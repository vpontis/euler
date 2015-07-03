def nth_num(n):
  x = (n-1)/4 
  nth = 1 + 4 * x * (x+1)
  y = n % 4
  return nth

total = 1
inc = 2
num = 3
for i in xrange(2, 2000+2):
  print num
  total += num
  num += inc
  if i % 4 == 0:
    inc += 2

print total

