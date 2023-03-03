import sys
import math
import string

SEPARATOR = " "

def better_round_with_trailing_zeros(val:float, n_digits:int = 0):
    val *= 10**n_digits
    result = int(val + (0.50002 if val >= 0 else -0.50002))
    return f"{(result / 10**n_digits):.2f}"

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

    density, volume = (float(val) for val in line.split(SEPARATOR))

    print(better_round_with_trailing_zeros(density*volume,2))