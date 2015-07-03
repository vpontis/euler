def get_grid():
  nums = []
  f = open('prob_11.txt')
  for line in f:
    nums.append(line)
  for i in range(len(nums)):
    nums[i] = [int(x) for x in nums[i].rstrip('\n').split(' ')]
  return nums

def product(nums):
  p = 1
  for num in nums:
    p *= num
  return p

def diagonal(x, y, grid, right=True):
  if right:
    sign = 1
  else:
    sign = -1

  diag = 1
  for i in xrange(4):
    disp = i * sign 
    diag *= grid[x + disp][y + disp]
  return diag



#biggest four adjacent numbers product
def eleven():
  grid = get_grid()
  biggest = 0

  # right diagonal 
  for i in range(20 - 3):
    for j in range(20 - 3):
      guess = diagonal(i, j, grid, True)
      if guess > biggest: biggest = guess
  print biggest
  
  # left diagonal
  for i in range(3, 20):
    for j in range(3, 20):
      guess = diagonal(i, j, grid, False)
      if guess > biggest: biggest = guess
  print biggest

  # in a row 
  for row in grid:
    for start_elem in range(20- 3):
      guess = product(row[start_elem:start_elem+4])
      if guess > biggest: biggest = guess
  print biggest 

  # in a column
  columns = zip(*grid)
  for column in columns:
    for start_elem in range(20 - 3):
      guess = product(column[start_elem:start_elem+4])
      if guess > biggest: biggest = guess
  print biggest

  return biggest

if __name__ == '__main__':
  print eleven()
