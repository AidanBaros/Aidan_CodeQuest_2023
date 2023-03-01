import sys

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    val = int(sys.stdin.readline().rstrip())
    for i in range(val):
        out = ""
        for j in range(val):
            out += "# "
        print(out.rstrip())