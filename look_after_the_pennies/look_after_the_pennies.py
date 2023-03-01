import sys
import math
import string

def better_round(val:float, n_digits:int = 0):
    val *= 10**n_digits
    result = int(val + (0.5 if val >= 0 else -0.5))
    return result / 10**n_digits

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    cases2 = int(sys.stdin.readline().rstrip())
    amount_in_savings = 0
    for caseNum2 in range(cases2):
        money = float(sys.stdin.readline().rstrip())
        charge = math.ceil(money)
        amount_in_savings += charge - money
        print(charge)
    result = better_round(amount_in_savings, 2)
    print(f"{result:.2f}")