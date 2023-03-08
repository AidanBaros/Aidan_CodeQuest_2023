"""System Module"""
import sys


def main():
    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        cases2 = int(sys.stdin.readline().rstrip())
        for _ in range(cases2):
            line = sys.stdin.readline().rstrip()
            words = line.split(" ")
            output = ""
            output += words[0][0]
            output += words[2][0]
            output += words[1][0]
            output = output.upper()
            print(output)

main()