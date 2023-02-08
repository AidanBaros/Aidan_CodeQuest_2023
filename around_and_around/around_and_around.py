import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

    distance = int(line)

    radius = 40_075/(math.pi*2)

    height = radius + distance

    new_circumference = math.pi*2*height

    print(round(new_circumference,1))