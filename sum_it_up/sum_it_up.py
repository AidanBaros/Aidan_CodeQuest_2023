"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        val1, val2 = (int(val) for val in line.split(" "))
        out = 0
        if val1 == val2:
            out = (val2 + val1)*2
        else:
            out = (val2 + val1)
        print(out)

main()