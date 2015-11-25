import Data.List
import qualified Data.Set as Set

primes = sieve [2..]
  where
      sieve (p:xs) = p : sieve [x|x <- xs, x `mod` p > 0]

firstPrimes = take 1000 primes

factorize x = [f | f <- firstPrimes, x `mod` f == 0]
numPrimeFactors :: Int -> Int
numPrimeFactors = length . factorize

nPF = numPrimeFactors

num = [x | x <- [1..], all (==4) $ map (\y -> nPF (x+y)) [0..3]]
