import math
def sum_divisors(x):
  total = 1
  y = 2
  while y < x:
    if x % y == 0:
        total += y
    y += 1
  return total

sum_divisors_dict = {}
amicable_nums = set()

for i in range(1, 10000):
  sum_divisors_dict[i] = sum_divisors(i)

for key, value in sum_divisors_dict.items():
  if key == sum_divisors_dict.get(value) and value == sum_divisors_dict.get(key) and value != key:
    amicable_nums.add(key)
    amicable_nums.add(value)

print amicable_nums
print sum(amicable_nums)