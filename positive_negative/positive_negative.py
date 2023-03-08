"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = int(sys.stdin.readline().rstrip())
        print("POSITIVE" if line > 0 else "NEGATIVE")


main()