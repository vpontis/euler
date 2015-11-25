import Data.List
import qualified Data.Set as Set

pentagons = [x*(3*x-1)/2 | x <- [1..]]
triangles = [x*(x+1)/2 | x <- [1..]]
hexagonal = [x*(2*x-1) | x <- [1..]]

pentSet = Set.fromList $ take takeNum pentagons
triangSet = Set.fromList $ take takeNum triangles
hexSet = Set.fromList $ take takeNum hexagonal

nums = Set.intersection (Set.intersection pentSet triangSet) hexSet

takeNum = 10000
firstPent = take takeNum pentagons

pair = [abs(x-y) | x <- firstPent, y <- firstPent, Set.member (x-y) pentSet, Set.member (x+y) pentSet]
