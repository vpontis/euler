f = open('p082_matrix.txt')
lines = f.readlines()
matrix = map(lambda line: map(int, line.strip().split(',')), lines)

dimension = 80

sol_matrix = [[float('inf')]*dimension + [float('inf')] for _ in xrange(dimension)]
sol_matrix.append([float('inf')]*(dimension+1))

for i in xrange(dimension):
    sol_matrix[i][0] = matrix[i][0]


# matrix is [y][x]
for _ in xrange(dimension):
    for y in xrange(dimension):
        for x in xrange(dimension):
            sol_matrix[y][x] = min(sol_matrix[y][x], matrix[y][x] + min(sol_matrix[y][x-1], sol_matrix[y-1][x], sol_matrix[y+1][x]))

elems = []
for i in xrange(dimension):
   elems.append(sol_matrix[i][-2]) 
print min(elems)
