import sys

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    cases2 = int(sys.stdin.readline().rstrip())
    total_sand = 0
    for caseNum2 in range(cases2):
        total_sand += int(sys.stdin.readline().rstrip())
    print(total_sand)