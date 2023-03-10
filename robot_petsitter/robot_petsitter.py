"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        directions = sys.stdin.readline().rstrip()
        ypos = 0
        xpos = 0
        for char in directions:
            if char == "U":
                ypos += 1
            elif char == "D":
                ypos -= 1
            elif char == "L":
                xpos -= 1
            elif char == "R":
                xpos += 1
        if ypos == 0 and xpos == 0:
            print("TRUE")
        else:
            print("FALSE")


main()