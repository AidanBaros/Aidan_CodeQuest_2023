import sys
import math
import string

SEPARATOR = "."

cases = int(sys.stdin.readline().rstrip())

dict_of_types = {}

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

    name, type = line.split(SEPARATOR)

    if type in dict_of_types:
        dict_of_types[type] += 1
    else:
        dict_of_types.update({type:1})

for key,value in dict_of_types.items():
    print(f"{key} {value}")

