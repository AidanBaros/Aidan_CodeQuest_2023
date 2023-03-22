"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        sides = line.split(", ")
        sides_int = []
        for side in sides: 
            sides_int.append(int(side))
        sides_int.sort()
        if sides_int[0] + sides_int[1] <= sides_int[2]:
            print("Not a Triangle")
        elif sides_int[0] == sides_int[1] and sides_int[1] == sides_int[2]:
            print("Equilateral")
        elif sides_int[0] == sides_int[1] and sides_int[1] != sides_int[2]:
            print("Isosceles")
        elif sides_int[0] != sides_int[1] and sides_int[1] == sides_int[2]:
            print("Isosceles")
        else:
            print("Scalene")


main()