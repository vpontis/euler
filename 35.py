import array
import itertools

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

primes_below_million = primes_up_to(1000000)
print 'got primes', len(primes_below_million)

circ_primes = []
for x in range(1, 1000000):
  circ_prime = True
  rotations = [[str(x)[i - j] for i in range(len(str(x)))] for j in range(len(str(x)))]
  for rot in rotations:
    if int(''.join(rot)) not in primes_below_million:
      circ_prime = False
      break
  if circ_prime: circ_primes.append(x)

print circ_primes
print len(circ_primes)

