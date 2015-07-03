def read_file(file_name):
  f = open(file_name)
  lines = []
  for line in f:
    lines.append(line)

  lines = [x.strip().split(' ') for x in lines]
  for i in range(len(lines)):
    lines[i] = [int(x) for x in lines[i]]
  return lines



lines = read_file('triangle.txt')
best_paths = [[0]*i for i in xrange(1, len(lines)+1)]

best_paths[0][0] = lines[0][0]
for i in xrange(1, len(best_paths)):
  previous_row = best_paths[i-1]
  row = best_paths[i]
  for j in xrange(len(row)):
    row[j] = lines[i][j] + max(previous_row[max(j-1, 0)], previous_row[min(j, len(previous_row)-1)])

  best_paths[i] = row

print max(best_paths[-1])
