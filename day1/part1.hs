-- Out puts a list of numbers, which I then sum up using a quick script.

import System.IO
import Data.Char

main :: IO ()
main = do
    line <- getLine
    case line of
        [] -> main
        x -> print (getLargestNum . replaceNums $ x) >> main

getLargestNum :: String -> Int
getLargestNum [] = error "empty string"
getLargestNum s =
    let digits = filter isDigit s
    in read $ head digits : last digits : []