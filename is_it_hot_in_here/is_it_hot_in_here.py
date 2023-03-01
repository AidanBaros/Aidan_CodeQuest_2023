import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    cases2 = int(sys.stdin.readline().rstrip())

    for caseNum2 in range(cases2):
        line = sys.stdin.readline().rstrip()

        temp, temp_type = line.split(SEPARATOR)

        temp = float(temp)
        if temp_type == "F":
            other_temp = (5/9)*(temp-32)
        else:
            other_temp = temp*(9/5)+32
        print(f"{line} = {round(other_temp,1)}", "C" if temp_type == "F" else "F")