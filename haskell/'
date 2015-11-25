import Data.List
import qualified Data.Set as Set

primes = sieve [2..]
  where
      sieve (p:xs) = p : sieve [x|x <- xs, x `mod` p > 0]

numDigits = length . show

fourDigits = dropWhile (\x -> numDigits x < 4) $ takeWhile (\x -> numDigits x < 5) primes

fourSet = Set.fromList fourDigits

permutationNums = flip filter fourDigits (\y -> (sumBools $ map (\x -> flip Set.member fourSet $ read x) (nub $ permutations $ show y)) > 3)

beginNums :: [String]
beginNums = sort . nub . map (sort . show) $ permutationNums

permutedGroups :: [[String]]
permutedGroups = map (\x -> filter (\y -> Set.member (read y) fourSet) (nub . permutations $ x)) beginNums

mode x = maximum . map length $ group x

answer = map (\g -> [x | x <- g, y <- g, z <- g, x /= y, y /= z, x /= z, (read z - read y) == (read y - read x)]) permutedGroups

boolToNum x = if x
              then 1
              else 0

sumBools bools = sum . map boolToNum $ bools
