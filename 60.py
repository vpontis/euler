'''
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''
from time import time

start_time = time()

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

primes = sorted(primes_up_to(10**7))

def two_primes_work(prime1, prime2):
    if int(str(prime1) + str(prime2)) not in primes:
        return False
    if int(str(prime2) + str(prime1)) not in primes:
        return False
    return True


first_four = set([3, 7, 109, 673])

for new_prime in primes:
    if new_prime <= 673:
        continue

    if all(map(lambda x: two_primes_work(x, new_prime), first_four)):
        print new_prime
        print sum(first_four) + new_prime
        break


end_time = time()
print 'Took this many seconds:', end_time - start_time