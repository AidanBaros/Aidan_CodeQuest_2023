import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    year = int(sys.stdin.readline().rstrip())

    month = 0
    date = 0

    a = year%19
    b = year%4
    c = year%7
    k = year//100
    p = (13+(8*k))//25
    q = k//4
    m = (15-p+k-q)%30
    n = (4+k-q)%7
    d = ((19*a) + m)%30
    e = ((2*b)+(4*c)+(6*d)+n)%7
    f = ((11*m)+11)%30

    date = 22+d+e

    if date <= 31:
        month = 3
    else:
        month = 4
        date -= 31
        if date == 25 and d == 28 and e == 6 and f < 19:
            date = 18
        elif date == 26 and d == 29 and e == 6:
            date = 19

    extra_zero = ""
    if date < 10:
        extra_zero = "0"

    print(f"{year}/0{month}/{extra_zero}{date}")
        