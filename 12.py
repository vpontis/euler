import math

def num_divisors(x):
  num = 2
  y = 2
  while y <= math.sqrt(x):
    if x % y == 0:
      if x/y == math.sqrt(x):
        num += 1
      else:
        num += 2
    y += 1
  return num

triag = 1
index = 1

while True:
  if num_divisors(triag) >= 500:
    break

  

  index += 1
  triag += index


print triag
