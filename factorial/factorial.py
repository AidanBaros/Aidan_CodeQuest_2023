import sys
import math
import string

SEPARATOR = ":"

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    num = int(sys.stdin.readline().rstrip())

    out = 1

    for i in range(num):
        out *= (i+1)

    print(out)