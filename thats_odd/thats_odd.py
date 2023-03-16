"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        num = int(sys.stdin.readline().rstrip())
        print("EVEN" if num%2 == 0 else "ODD")

main()