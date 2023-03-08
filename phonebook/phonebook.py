"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        number, format = line.split(" ")
        if format == "PARENTHESES":
            print(f"({number[:3]}) {number[3:6]}-{number[6:]}")
        elif format == "DASHES":
            print(f"{number[:3]}-{number[3:6]}-{number[6:]}")
        elif format == "PERIODS":
            print(f"{number[:3]}.{number[3:6]}.{number[6:]}") 


main()