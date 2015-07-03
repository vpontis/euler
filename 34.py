'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''
def fact(n):
  tot = 1
  for i in range(1, int(n) + 1):
    tot *= i
  return tot


facts = set()

for i in range(11, 5362880):
  if sum([fact(x) for x in list(str(i))]) == i:
    facts.add(i)

print sorted(facts)
print sum(facts)