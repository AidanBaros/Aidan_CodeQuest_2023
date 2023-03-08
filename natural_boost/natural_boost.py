"""System Module"""
import sys
import math


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        angle = float(sys.stdin.readline().rstrip())
        radius = 6_370_000 * math.cos(math.radians(angle))
        out = 2*math.pi*radius//86_400
        print(int(out))


main()