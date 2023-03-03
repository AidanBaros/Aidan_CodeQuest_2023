import sys

def better_round_with_trailing_zeros(val:float, n_digits:int = 0):
    val *= 10**n_digits
    result = int(val + (0.5000001 if val >= 0 else -0.5000001))
    return f"{(result / 10**n_digits):.2f}"

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    bill = float(line[1:])

    print(f"Total of the bill: {line}")
    print(f"15% = ${better_round_with_trailing_zeros(bill*0.15,2)}")
    print(f"18% = ${better_round_with_trailing_zeros(bill*0.18,2)}")
    print(f"20% = ${better_round_with_trailing_zeros(bill*0.20,2)}")