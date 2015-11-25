import qualified Data.Set as Set
primes = sieve [2..]
  where
      sieve (p:xs) = p : sieve [x|x <- xs, x `mod` p > 0]

primeSet = Set.fromList $ take 5000 primes

squares = map (*2) $ map (^2) [1..]

oddComposites = Set.fromList $ take 5000 $ filter (not . flip Set.member primeSet) $ filter odd [1..]

sumSquareAndPrime = Set.fromList [pr + sq | pr <- take 2000 primes, sq <- take 2000 squares]

nums = Set.difference oddComposites sumSquareAndPrime
