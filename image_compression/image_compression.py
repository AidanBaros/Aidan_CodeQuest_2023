import sys

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    cases2 = int(sys.stdin.readline().rstrip())
    list_of_vals = []
    for caseNum2 in range(cases2):
        list_of_vals.append(float(sys.stdin.readline().rstrip()))
    for i in range(cases2):
        print(round(((list_of_vals[i]-min(list_of_vals))/(max(list_of_vals)-min(list_of_vals)))*255))