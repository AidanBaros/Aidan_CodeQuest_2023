import sys
import math

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = int(sys.stdin.readline().rstrip())
    num = line

    count = 0

    while num != 1:
        count += 1
        if num % 2 == 0:
            num = num / 2
        else:
            num = (num*3) + 1
        

    print(f"{line}:{count + 1}")