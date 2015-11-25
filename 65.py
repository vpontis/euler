iseven = lambda x: x % 2 == 0

from fractions import Fraction

def e_seq(n):
    yield 1
    num = 2
    for i in xrange(1, n-1):
        if iseven(i):
            yield 1
            yield 1
        else:
            yield num 
            num += 2

first_100 = [i for i in e_seq(100)][:99]


def generate_num(nums):
    total_num = Fraction(0)
    nums.reverse()
    for i in nums:
        total_num = Fraction(1, Fraction(i) + total_num)
    return total_num

print 1+generate_num([2]*2)
print 1+generate_num([2]*3)
print 1+generate_num([2]*4)
print 2+generate_num(first_100)
