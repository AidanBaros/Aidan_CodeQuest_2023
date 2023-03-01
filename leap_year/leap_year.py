import sys

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    cases2 = int(sys.stdin.readline().rstrip())
    for caseNum2 in range(cases2):
        year = sys.stdin.readline().rstrip()
        is_leap_year = "No"
        year = int(year)
        if year < 1582:
            pass
        elif year%4 != 0:
            pass
        elif year% 100 != 0:
            is_leap_year = "Yes"
        elif year %400 != 0:
            pass
        else:
            is_leap_year = "Yes"
        print(is_leap_year)