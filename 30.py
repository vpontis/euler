def sum_fifth_power(num):
  powers = map(lambda x: x**5, [int(x) for x in list(str(num))])
  return sum(powers)

nums = []
for i in range(2, 100000*100):
  if sum_fifth_power(i) == i:
    nums.append(i)

print nums
print sum(nums)