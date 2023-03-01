import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

    x, y = line.split(SEPARATOR)

    print("false" if (x == "false" and y == "true") or (y == "false" and x == "true") else "true")
