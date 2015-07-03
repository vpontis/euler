'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

'''

import math
import time

start = time.time()

fraction = ''

for i in xrange(1, 10**10):
    if len(fraction) > 1000000: break
    fraction += str(i)


print fraction[:60]


result = int(fraction[0]) * int(fraction[10-1]) * int(fraction[100-1]) * int(fraction[1000-1]) * int(fraction[10000-1]) * int(fraction[100000-1]) * int(fraction[1000000-1])

print result


end = time.time()
print end - start