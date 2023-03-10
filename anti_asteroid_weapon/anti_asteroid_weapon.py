"""System Module"""
import sys
import math


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        cases2 = int(sys.stdin.readline().rstrip())
        data = {}
        for _ in range(cases2):
            line = sys.stdin.readline().rstrip()
            val1, val2 = (int(val) for val in line.split(" "))
            distance = math.sqrt((val1*val1)+(val2*val2))
            data.update({distance:[val1,val2]})
        sorted(data)
        for key in sorted(list(data.keys())):
            print(*data[key])



main()