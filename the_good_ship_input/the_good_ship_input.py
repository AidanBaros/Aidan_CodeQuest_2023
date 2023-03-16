"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        nums = sys.stdin.readline().rstrip()
        val1, val2 = (int(val) for val in nums.split(" "))
        shipyard = []
        ship = []
        check_list = []
        for i in range(val1):
            line = sys.stdin.readline().rstrip()
            shipyard.append(line)
        for i in range(val2):
            line = sys.stdin.readline().rstrip()
            ship.append(line)
        shipyard.sort(key=lambda s: s.lower())
        ship.sort(key=lambda s: s.lower())
        for s in shipyard:
            if s not in ship:
                print(s)

main()