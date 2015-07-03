'''
The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
'''

end_num = 1000

ten_to_ten = 10**10
last_ten = 0

for num in xrange(1, end_num + 1):
    last_ten += (num**num)%ten_to_ten
    last_ten %= ten_to_ten

print last_ten