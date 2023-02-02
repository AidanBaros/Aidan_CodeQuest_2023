import sys
import math
import string

SEPARATOR = ":"

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    for caseNum2 in range(cases):
        line2 = sys.stdin.readline().rstrip()

        x, y = (float(val) for val in line2.split(SEPARATOR))

        
