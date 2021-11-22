# Do not remove
import sys, json
# Read every line
'''lines = sys.stdin.readlines()
lines = json.loads(lines[0])'''

lines = [["papier", "papier","pierre"], ["pierre", "ciseaux","papier"]]

points1 = 0
points2 = 0

for i in range(0,3):
    if lines[0][i] == "papier" and lines[1][i] == "pierre":
        points1 += 1
        print("J1 a gagné la manche", i+1, ".")
    elif lines[0][i] == "pierre" and lines[1][i] == "ciseaux":
        points1 += 1
        print("J1 a gagné la manche", i+1, ".")
    elif lines[0][i] == "ciseaux" and lines[1][i] == "papier":
        points1 += 1
        print("J1 a gagné la manche", i+1, ".")
    elif lines[0][i] == "pierre" and lines[1][i] == "papier":
        points2 += 1
        print("J2 a gagné la manche", i+1, ".")
    elif lines[0][i] == "ciseaux" and lines[1][i] == "pierre":
        points2 += 1
        print("J2 a gagné la manche", i+1, ".")
    elif lines[0][i] == "papier" and lines[1][i] == "ciseaux":
        points2 += 1
        print("J2 a gagné la manche", i+1, ".")
    elif (lines[0][i] == "papier" and lines[1][i] == "papier") or (lines[0][i] == "ciseaux" and lines[1][i] == "ciseaux") or (lines[0][i] == "pierre" and lines[1][i] == "pierre"):
        points1 += 1
        points2 += 1
        print("Match nul.")

if points1 > points2:
    print("J1 a gagné.")
elif points2 > points1:
    print("J2 a gagné.")
elif points1 == points2:
    print("Parie nul.")