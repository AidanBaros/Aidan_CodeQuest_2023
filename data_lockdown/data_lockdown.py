import sys
import math
import string

SEPARATOR = " "
SEPARATOR2 = "."

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    cases2 = int(sys.stdin.readline().rstrip())
    for caseNum2 in range(cases2):
        line = sys.stdin.readline().rstrip()

        domain, ammoun_of_data = line.split(SEPARATOR)

        ammoun_of_data = int(ammoun_of_data)

        domain_parts = (list(domain.split(SEPARATOR2)))

        if ammoun_of_data > 1000:
            if ("lmco" in domain_parts) and ("com" in domain_parts):
                pass
            else:
                print(line)
            