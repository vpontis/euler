f = open('p081_matrix.txt')
lines = f.readlines()
matrix = map(lambda line: map(int, line.strip().split(',')), lines)

sol_matrix = [[None]*80 + [float('inf')] for _ in xrange(80)]
sol_matrix.append([float('inf')]*81)

sol_matrix[0][0] = matrix[0][0]

# matrix is [x][y]

for y in xrange(80):
    for x in xrange(80):
        if x == 0 and y == 0:
            continue
        sol_matrix[x][y] = matrix[x][y] + min(sol_matrix[x-1][y], sol_matrix[x][y-1])

print sol_matrix[-2][-2]
         
