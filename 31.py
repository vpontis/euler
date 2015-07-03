## different ways of creating coins
def make_coins(coin_set, amount):
  coin_list = sorted(coin_set)
  N = len(coin_list)
  K = amount

  # use only a certain number of coins to create an exact amount. our parameters will be n -- number of coins and k -- amount we are trying to create
  # for a specific n, k pair we will look at the nth valued coin and try to create that amount
  
  # dp is going to be a matrix that is num coins tall and amount wide

  dp = [[0]*N for i in xrange(K+1)]


  for n in xrange(N):
    for k in xrange(1, K+1):
      coin_amount = coin_list[n]
      if n > 0: dp[k][n] = dp[k][n-1]
      if k % coin_amount == 0: dp[k][n] += 1
      prev_amount = k - coin_amount
      while prev_amount >= 0:
        dp[k][n] += dp[prev_amount][n-1]
        prev_amount -= coin_amount

  return dp

coins = make_coins([1,2,5,10,20,50,100,200], 200)
for i in range(len(coins)):
  print coins[i], i
print coins[-1][-1]