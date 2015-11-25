import Data.Csv
import Data.List
import Data.Matrix
import System.IO
import Data.List.Split
import qualified Data.ByteString.Lazy as BL
import qualified Data.Vector as V

shortestPath 1 1 mtx = getElem 1 1 mtx
shortestPath i 1 mtx = shortestPath (i-1) 1 mtx + getElem i 1 mtx
shortestPath 1 j mtx = shortestPath 1 (j-1) mtx + getElem 1 j mtx
shortestPath i j mtx = min (shortestPath i (j-1) mtx + getElem i j mtx)  (shortestPath (i-1) j mtx + getElem i j mtx)

process :: String -> [[Int]]
process contents = fromLists <- map (\x -> map read $ splitOn "," x) $ take 80 $ splitOn "\n" contents

fileName = "p081_matrix.txt"

main = do
  contents <- readFile fileName
  -- matrix = fromLists $ process contents
  -- mList 3 3 [1..]
  putStrLn "Hello"
