import sys

SEPARATOR = " "

def better_round(val:float, n_digits:int = 0):
    val *= 10**n_digits
    result = int(val + (0.5 if val >= 0 else -0.5))
    return int(result / 10**n_digits)

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

    volume, fill, leak = (int(val) for val in line.split(SEPARATOR))

    print(better_round((volume/(fill-leak))*leak))