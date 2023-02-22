import sys
import math
import string

SEPARATOR = ","

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line1 = sys.stdin.readline().rstrip()
    line2 = sys.stdin.readline().rstrip()

    last_year_donors = list(line1.split(SEPARATOR))
    this_year_donors = list(line2.split(SEPARATOR))

    only_last_year = []
    both_years = []
    only_this_year = []

    for donor in last_year_donors:
        if donor not in this_year_donors:
            only_last_year.append(donor)
        elif donor in this_year_donors:
            both_years.append(donor)
    for donor in this_year_donors:
        if donor not in last_year_donors:
            only_this_year.append(donor)

    only_this_year.sort()
    both_years.sort()
    only_last_year.sort()

    for i in range(len(only_last_year)):
        print(only_last_year[i], end="")
        if i+1 != len(only_last_year):
            print(",",end="")
    print()
    for i in range(len(both_years)):
        print(both_years[i], end="")
        if i+1 != len(both_years):
            print(",",end="")
    print()
    for i in range(len(only_this_year)):
        print(only_this_year[i], end="")
        if i+1 != len(only_this_year):
            print(",",end="")
    print()