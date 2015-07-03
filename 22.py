import string

def read_file(filename):
  f = open(filename)
  names = []
  for line in f: names.append(line)
  names = [str(x.strip('"')) for x in names[0].split(',')]
  names = sorted(names)
  return names

def name_to_int(name):
  nums = map(lambda x: string.ascii_uppercase.index(x) + 1, list(name))
  return sum(nums)

names = read_file('names.txt')
name_scores = []

for i in xrange(len(names)):
  number = name_to_int(names[i])
  name_scores.append(number*(i+1))

print sum(name_scores)