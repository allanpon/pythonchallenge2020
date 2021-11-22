# Do not remove
import sys, json
# Read every line
'''lines = sys.stdin.readlines()
lines = json.loads(lines[0])'''

lines = ["épée"]

point = {"a": 1 , "b": 3 , "c": 3 , "d": 2 ,
         "e": 1 , "f": 4 , "g": 2 , "h": 4 ,
         "i": 1 , "j": 8 , "k": 10, "l": 1 ,
         "m": 2 , "n": 1 , "o": 1 , "p": 3 ,
         "q": 8, "r": 1  , "s": 1 , "t": 1 ,
         "u": 1 , "v": 4 , "w": 10, "x": 10,
         "y": 10, "z": 10}

def scrabble_point(word):
    total = 0

    for i in word:
        if i in point:
            i = i.lower(); 
            total = total + point[i]
        else:
            total -= total

    print(total)

print(scrabble_point(lines[0]))
