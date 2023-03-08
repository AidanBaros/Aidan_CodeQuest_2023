"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = int(sys.stdin.readline().rstrip())
        print("PASS" if line >= 70 else "FAIL")


main()