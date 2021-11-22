# Do not remove
import sys, json
# Read every line
'''lines = sys.stdin.readlines()
lines = json.loads(lines[0])'''

lines = [["The python"],["drinks", "plays with"],["a cup of java", "a ruby"]]

for i in lines[0]:
    for j in lines[1]:
        for k in lines[2]:
            print(i,j,k)