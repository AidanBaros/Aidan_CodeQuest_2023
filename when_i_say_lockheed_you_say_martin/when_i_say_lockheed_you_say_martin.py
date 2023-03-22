"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        num = int(sys.stdin.readline().rstrip())
        if num%3 == 0 and num%7 == 0:
            print("LOCKHEEDMARTIN",end="")
        elif num%3 == 0:
            print("LOCKHEED",end="")
        elif num%7 == 0:
                print("MARTIN",end="")
        else:
            print(num,end="")
        print()


main()