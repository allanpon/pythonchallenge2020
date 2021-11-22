# Do not remove
import sys, json
# Read every line
'''lines = sys.stdin.readlines()
lines = json.loads(lines[0])'''

lines = [6,8,10]

if lines[0]*lines[0] + lines[1]*lines[1] == lines[2]*lines[2] or lines[1]*lines[1] + lines[2]*lines[2] == lines[0]*lines[0] or lines[0]*lines[0]+lines[2]*lines[2] == lines[1]*lines[1]:
    print("Ce triangle est rectangle.")
else:
    print("Ce triangle n'est pas rectangle.")