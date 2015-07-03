'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

examples = set()

def try_cancel(numstr, denstr, ratio):
  for i in range(2):
    for j in range(2):
      num = float(numstr[i])
      den = float(denstr[j])
      if numstr[1-i] != denstr[1-j]: continue
      if den == 0.0 or num == 0.0: continue
      if num/den == ratio:
        return True
  return False

print try_cancel('49', '98', float(49)/float(98)), 'should be true'

for den in xrange(11, 100):
  for num in xrange(10, den):
    numstr = str(num)
    denstr = str(den)

    if set(list(numstr)).isdisjoint(set(list(denstr))):
      continue

    if num % 10 == 0 and den % 10 == 0: continue
    if num == den: continue

    ratio = float(num)/float(den)

    if try_cancel(numstr, denstr, ratio):
      examples.add((num, den, num/float(den)))


print examples