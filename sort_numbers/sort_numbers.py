"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        numbers = [int(val) for val in line.split(",")]
        numbers.sort()
        print(*numbers,sep=",") 


main()