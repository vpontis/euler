import Data.List

oneThroughTen x = sort x == "123456789"

pandigitalNum x = if any oneThroughTen strs then
                    read ([x | x <- strs, length x == 9] !! 0) :: Int
                  else
                    0 :: Int
                  where strs = scanl (++) "" $ map show [x, x*2..x*10]

maxNum = maximum $ map pandigitalNum [1..10000]


