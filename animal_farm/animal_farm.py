import sys
import math
import string

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

    x, y, z = (int(val) for val in line.split(SEPARATOR))

    print((x*2)+(y*4)+(z*4))