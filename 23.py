import math

def sum_divisors(x):
  total = 1
  y = 2
  while y < x:
    if x % y == 0:
        total += y
    y += 1
  return total

abundant_nums = filter(lambda x: sum_divisors(x) > x , xrange(1, 28124))

possible_sums = [False]*28124
possible_sums[0] = True

print len(abundant_nums)

for i in xrange(len(abundant_nums)):
  for j in xrange(len(abundant_nums)):
    y = abundant_nums[i]+abundant_nums[j]
    if y >= len(possible_sums): continue
    possible_sums[y] = True

total = 0
not_sums = []
for x in xrange(len(possible_sums)):
  if possible_sums[x] == False:
    not_sums.append(x)
    total += x

print not_sums
print total