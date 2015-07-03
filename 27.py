def primes_up_to(n):
  import array
  arr = array.array('i', [0]*(n-1))
  primes = set()

  index = 0
  while index < len(arr):
    num = index + 2
    # add prime to set
    primes.add(num)

    # get multiples of prime and mark them
    mark = index
    while mark < len(arr):
      arr[mark] = 1
      mark += num

    # increment index
    while arr[index] != 0:
      index += 1
      if index == len(arr): break
  return primes

primes = primes_up_to(1000000)
print 'got primes'

def num_primes(a, b):
  if b not in primes: return 0
  num = b
  for i in range(1, 1000000):
    num += 2 * i - 1
    num += a
    if num not in primes: return i

print num_primes(1, 41), ' should be 40'
print num_primes(-79, 1601), ' should be 80'


eligible_primes = primes_up_to(1000)
pos_primes = eligible_primes.copy()
negs = set()
for prime in eligible_primes:
  negs.add(-prime)
eligible_primes = eligible_primes.union(negs)


# import pdb
# pdb.set_trace()

# print eligible_primes
# print pos_primes

best_a = 0
best_b = 0
best_num = 0

times = 0
for a in eligible_primes:
  times += 1
  if times % 10 == 0: print times
  for b in pos_primes:
    guess = num_primes(a, b)
    if guess > best_num:
      best_num = guess
      best_a = a
      best_b = b

print best_num
print best_a, best_b, best_b * best_a