orderings = set()

f = open('p079_keylog.txt')
lines = map(lambda x: x.strip(), f.readlines())

for line in lines:
    orderings.add((line[0], line[1]))
    orderings.add((line[1], line[2]))
    orderings.add((line[0], line[2]))

output = ''

print sorted(list(set(map(lambda x: x[0], orderings))))
print sorted(list(set(map(lambda x: x[1], orderings))))
while orderings:
    rights = set(map(lambda x: x[1], orderings))
    lefts = set(map(lambda x: x[0], orderings))
    no_into = lefts - rights
    next_num = list(no_into)[0]
    orderings = set(filter(lambda x: x[0] != next_num, orderings))
    output += next_num
    print output

