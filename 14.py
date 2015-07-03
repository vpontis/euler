from array import *

million = int(1E6)
collatz_length = array('i', [-1]*million)
collatz_length[1] = 1

def collatz_length_of(num, biggest_update):
  if num <= biggest_update: return collatz_length[num]

  if num % 2 == 0: length = 1 + collatz_length_of(num/2, biggest_update)
  else: length = 1 + collatz_length_of(3*num + 1, biggest_update)

  if num < million: collatz_length[num] = length
  return length


longest = (1,1)
i = 2
while i < 1E6:
  guess = collatz_length_of(i, i-1)
  if guess > longest[0]:
    longest = (guess, i)
  i += 1

print longest 