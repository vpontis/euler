from decimal import *
import re
getcontext().prec = 5000


def smallest_cycle_length(seq):
    for i in xrange(1, len(seq)/2):
        i_is_cycle = True
        for j in xrange(len(seq) - i):
            if seq[j] != seq[j + i]:
                i_is_cycle = False
                break
        if i_is_cycle: return i
    return 0

print smallest_cycle_length('10101010'), 'should be 2'
print smallest_cycle_length('11111'), 'should be 1'
print smallest_cycle_length('123123123'), 'should be 3'
print smallest_cycle_length('123123412312'), 'should be 0'
print smallest_cycle_length(str(Decimal(1)/Decimal(251))[2:]), 'should be 50'


def cycle_length(seq):
    length = 0
    for i in xrange(15):
        length = max(smallest_cycle_length(seq[i:]), length)
    return length

max_length = 1
best_i = 1
for i in range(2, 1000):
    if i % 100 == 0: print i
    seq = str(Decimal(1)/Decimal(i))[2+50:]
    guess = smallest_cycle_length(seq)
    if guess > max_length:
        best_i = i
        max_length = guess
print max_length, best_i


