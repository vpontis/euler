import Data.List

pandigitalNums = permutations "1234567890"

subsetDivisible x start divisor = mod (read $ drop start . take (start+3) $ x) divisor == 0

sD = subsetDivisible

rightNum x = (sD x 1 2) && (sD x 2 3) && (sD x 3 5) && (sD x 4 7) && (sD x 5 11) && (sD x 6 13) && (sD x 7 17)

num = sum $ map read $ filter rightNum pandigitalNums
