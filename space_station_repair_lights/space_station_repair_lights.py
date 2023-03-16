"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        checks = line.split(" ")
        if checks[0] == "BROKEN" and checks[1] == "BROKEN":
            print("blue",end=' ')
        elif checks[0] == "WORKING" and checks[1] == "BROKEN":
            print("red",end=' ')
        elif checks[0] == "BROKEN" and checks[1] == "WORKING":
            print("green",end=' ')
        elif checks[0] == "WORKING" and checks[1] == "WORKING":
            print("off",end=' ')
        if checks[2] == "BROKEN" and checks[3] == "BROKEN":
            print("blue")
        elif checks[2] == "WORKING" and checks[3] == "BROKEN":
            print("red")
        elif checks[2] == "BROKEN" and checks[3] == "WORKING":
            print("green")
        elif checks[2] == "WORKING" and checks[3] == "WORKING":
            print("off")


main()