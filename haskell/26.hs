import Data.List

oneThroughTen x y = (sort (show x ++ show y ++ show (x*y))) == "123456789"

pandigitals = [ a * b | a <- [1..50], b <- [1..2000], oneThroughTen a b ]

pandigitalSum = sum (nub pandigitals)
