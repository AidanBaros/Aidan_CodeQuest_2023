import sys
import math
import string

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()

    one_inch_bricks, five_inch_bricks, wall_length = (int(val) for val in line.split(SEPARATOR))

    if ((five_inch_bricks*5) + one_inch_bricks) < wall_length:
        print("false")
    elif ((five_inch_bricks*5) + one_inch_bricks) == wall_length:
        print("true")
    else:
        current_length = 0
        while current_length <= wall_length - 5 and five_inch_bricks != 0:
            current_length += 5
            five_inch_bricks -= 1
        current_length += one_inch_bricks
        if current_length < wall_length:
            print("false")
        else:
            print("true")