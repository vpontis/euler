f = open('p083_matrix.txt')
lines = f.readlines()
matrix = map(lambda line: map(int, line.strip().split(',')), lines)

dimension = 80

sol_matrix = [[float('inf')]*dimension + [float('inf')] for _ in xrange(dimension)]
sol_matrix.append([float('inf')]*(dimension+1))

sol_matrix[0][0] = matrix[0][0]

# matrix is [y][x]
for _ in xrange(dimension):
    for y in xrange(dimension):
        for x in xrange(dimension):
            sol_matrix[y][x] = min(sol_matrix[y][x], matrix[y][x] + min(sol_matrix[y][x-1], sol_matrix[y-1][x], sol_matrix[y+1][x], sol_matrix[y][x+1]))

print sol_matrix[-2][-2]
