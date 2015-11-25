import Data.List

pandigital n = (sort $ show n) == ['1'..(show len !! 0)]
              where len = length $ show n

primes = sieve [2..]
  where
      sieve (p:xs) = p : sieve [x|x <- xs, x `mod` p > 0]

firstPrimes = take 5000 primes

probablyPrime x = not $ any (==0) $ map (mod x) firstPrimes

maxPan :: Integer
maxPan = maximum $ filter probablyPrime (map (read::String->Integer) $  permutations "1234567")
