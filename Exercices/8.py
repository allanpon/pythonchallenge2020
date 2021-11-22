# Do not remove
import sys, json
# Read every line
lines = sys.stdin.readlines()
lines = json.loads(lines[0])

print(lines)