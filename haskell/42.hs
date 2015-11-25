import Data.List
import Data.List.Split
import qualified Data.Set as Set
import Control.Monad
import System.IO

triangleNums = map (\x -> floor $ (x^2+x)/2) [1..]

triangleSet = Set.fromList $ take 1000 triangleNums

letterToNum x = elemIndex x ['@','A'..'Z']

wordToNum x = sum $ map (\y -> maybe 0 id y) $ map letterToNum x

countTriangleWords x = length $ filter (\y -> Set.member y triangleSet) $ map wordToNum $ splitOn "," x

main = do
  handle <- openFile "p042_words.txt" ReadMode
  contents <- hGetContents handle
  let num = countTriangleWords contents
  print num
  hClose handle

