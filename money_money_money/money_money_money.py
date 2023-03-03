"""System Module"""
import sys

def better_round(val:float, n_digits:int = 0):
    val *= 10**n_digits
    result = int(val + (0.5 if val >= 0 else -0.5))
    return result / 10**n_digits

def main():
    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        country = sys.stdin.readline().rstrip()
        data = {}
        cases2 = int(sys.stdin.readline().rstrip())
        for _ in range(cases2):
            line = sys.stdin.readline().rstrip()
            money, year = line.split(" ")
            money = better_round(float(money))
            data.update({year:money})
        print(f"{country}:")
        dict(sorted(data.items()))
        for key in data.keys():
            #print(f"{key} {"*" for }")
            pass


main()