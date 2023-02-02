import sys
import math
import string

SEPARATOR = "|"

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

    x, y = ((val) for val in line.split(SEPARATOR))

    ListX = []
    ListY = []

    for char in x: ListX.append(char)
    for char in y: ListY.append(char)
    ListX.sort()
    ListY.sort()

    if x == y:
        print(f"{x}|{y} = NOT AN ANAGRAM")
    elif ListX == ListY:
        print(f"{x}|{y} = ANAGRAM")
    else:
        print(f"{x}|{y} = NOT AN ANAGRAM")
