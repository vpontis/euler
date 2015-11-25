import Data.List

doubleUs x y = doubleMe x + doubleMe y
doubleMe x = x + x
doubleSmall x = if x > 100
                  then x
                  else doubleMe x

oneThroughTen x y = (sort (show x ++ show y ++ show (x*y))) == "123456789"

pandigitals = [ a * b | a <- [1..50], b <- [1..2000], oneThroughTen a b ]

pandigitalSum = sum (nub pandigitals)
