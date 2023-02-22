import sys
import math

cases = int(sys.stdin.readline().rstrip())

def better_round(val:float, n_digits:int = 0):
    val *= 10**n_digits
    result = int(val + (0.5 if val >= 0 else -0.5))
    return result / 10**n_digits

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    money = float(line[1:])

    quarters = int(money/0.25)
    money = better_round(money % 0.25,2)
    dimes = int(money/0.1)
    money = better_round(money % 0.1,2)
    nickles = int(money/0.05)
    money = better_round(money % 0.05,2)
    pennies = int(money/.01)



    print(f"{line}")
    print(f"Quarters={quarters}")
    print(f"Dimes={dimes}")
    print(f"Nickels={nickles}")
    print(f"Pennies={pennies}")
    