'''
Problem 52: Permuted multiples
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

'''

test_num = 1

def same_digits(first_num, second_num):
    return sorted(list(str(first_num))) == sorted(list(str(second_num)))

def permuted_mults(num):
    for i in xrange(2, 7):
        if not same_digits(num, i*num):
            return False
    return True

while True:
    if permuted_mults(test_num):
        break
    test_num += 1

print test_num
