import sys
import math
import string

SEPARATOR = "|"

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

    greeting, response = (list(val.lower()) for val in line.split(SEPARATOR))
    
    flag = True
    for c in response:
        if c in string.ascii_lowercase:
            if c not in greeting:
                flag = False

    if flag:
        print("That's my secret contact!")
    else:
        print("You're not a secret agent!")