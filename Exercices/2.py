# Do not remove
import sys, json
# Read every line
'''lines = sys.stdin.readlines()
lines = json.loads(lines[0])'''

lines = ["omniscient","cimentons"]

if sorted(lines[0]) == sorted(lines[1]):
    print("Ces deux mots sont des anagrames.")
else:
    print("Ces deux mots ne sont pas des anagrames.")