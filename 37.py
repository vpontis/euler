import array

def primes_up_to(n):
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

max_val = 1000000

primes = primes_up_to(max_val)

trunc_primes = []
for i in xrange(10, max_val):
  trunc_prime = True
  if i not in primes:
    continue
  for j in xrange(1, len(str(i))):
    if int(str(i)[j:]) not in primes:
      trunc_prime = False
      break
    if int(str(i)[:j]) not in primes:
      trunc_prime = False
      break

  if trunc_prime: trunc_primes.append(i)

print len(trunc_primes)
print sum(trunc_primes)