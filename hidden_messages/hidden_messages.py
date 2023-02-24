import sys

SEPARATOR = "-"

cases = int(sys.stdin.readline().rstrip())
key = sys.stdin.readline().rstrip()

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

    x, y = (float(val) for val in line.split(SEPARATOR))