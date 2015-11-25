import Data.List
import qualified Data.Set as Set

primes = sieve [2..]
  where
      sieve (p:xs) = p : sieve [x|x <- xs, x `mod` p > 0]

million = 10^6

smallPrimes = takeWhile (< 10000) primes

isPrime x = all (/=0) . map (mod x) $ smallPrimes

slice from to xs = take (to - from + 1) (drop from xs)

len = 50

allSlices l = (filter (\x -> isPrime x && x < million) $ map (\x -> sum . slice x (x+l) $ primes) [1..(length smallPrimes) - l])


-- answer = maximum . filter (\x -> allSlices x /= 0) $ [100..1000]
