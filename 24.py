import itertools

def perms(elems, num):
  perms = itertools.permutations(elems)
  i = 1
  for perm in perms:
    if i == num:
      return perm
    i += 1


print perms([0,1,2,3,4,5,6,7,8,9], 1000000)