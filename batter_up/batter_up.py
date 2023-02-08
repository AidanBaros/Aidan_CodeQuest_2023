import sys
import math
import string

SEPARATOR = ":"
SEP2 = ","

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

    name, bats = line.split(SEPARATOR)
    hits = bats.split(SEP2)
    bases = 0
    total_hits = 0
    for i, hit in enumerate(hits):
        if hit == "K":
            total_hits += 1
        elif hit == "1B":
            bases += 1
            total_hits += 1
        elif hit == "2B":
            bases += 2
            total_hits += 1
        elif hit == "3B":
            bases += 3
            total_hits += 1
        elif hit == "HR":
            bases += 4
            total_hits += 1
    
    if total_hits != 0:
        total = round((bases/total_hits),3)

    else:
        total = 0
    
    print(f"{name}={total:.3f}")