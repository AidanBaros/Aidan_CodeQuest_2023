import sys
import math
import string

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

    scores_list = list(int(val) for val in line.split(SEPARATOR))
    scores_list.sort()
    print(scores_list[-1])