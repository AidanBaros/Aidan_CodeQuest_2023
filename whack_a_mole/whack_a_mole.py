"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        data = line.split(" ")
        out = ""
        for i, space in enumerate(data):
            if space == "M":
                out += f"{i+1} "
        print(out.rstrip())


main()